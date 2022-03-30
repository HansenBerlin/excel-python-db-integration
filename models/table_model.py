import itertools
from copy import deepcopy
from controller.data_validator import DataValidator
from models import column_model as cm
from common import database_exceptions as ex
from models.database_model_singleton import DatabaseModelSingleton
from controller.random_data_creator import RandomDataCreator
from collections import Counter


class TableModel:
    def __init__(self, random_data_gen: RandomDataCreator, validator: DataValidator,
                 table_name: str, schema_name: str = '', is_connection_table: bool = False):
        self.name = table_name
        self.schema = schema_name
        self.__columns = {}
        self.__is_col_adding_locked = False
        self.__rows = []
        self.__id_count = 0
        self.__validator = validator
        self.__rnd_gen = random_data_gen
        self.__is_connection_table = is_connection_table
        parent_db = DatabaseModelSingleton()
        parent_db.add_table(self)

    def add_columns(self, columns: list[cm]):
        for col in columns:
            if col.is_fk:
                tabref, colref = col.fk_model.ref_table, col.fk_model.ref_col
                if not self.__validator.is_valid_foreign_key(tabref, colref):
                    raise ex.ForeignKeyReferenceNotFoundException(f'reftable: {tabref}, refcolumn: {colref}, column: {col.name}')
            self.__add_column(col)

    def add_random_datasets(self, datasets_count: int):
        self.__is_col_adding_locked = True
        temp_set = []
        for i in range(datasets_count):
            self.__id_count += 1
            data_set = []
            for v in self.__columns.values():
                if v.is_pk:
                    data = self.__id_count
                elif v.is_fk:
                    data = self.__rnd_gen.create_matching_random_data(v.rand_data_info, v.fk_model.ref_count)
                else:
                    data = self.__rnd_gen.create_matching_random_data(v.rand_data_info, datasets_count)

                data_set.append(data)

                if v.limit_occurences:
                    temp_set.append(f'{v.name} {data}')
                    test = Counter(temp_set)
                    if test[f'{v.name} {data}'] > v.max_occurences:
                        data_set = []

            if len(data_set) > 0:
                self.__rows.append(data_set)

    def get_columns_list(self):
        ls = []
        for v in self.__columns.values():
            ls.append(deepcopy(v))
        return ls

    def get_rows_dict(self):
        return deepcopy(self.__rows)

    def remove_duplicates(self):
        if self.__is_connection_table:
            r = self.__rows
            r.sort()
            self.__rows = list(r for r, _ in itertools.groupby(r))

    def __add_column(self, column: cm):
        if self.__is_col_adding_locked:
            raise ex.RowAddingLockedException(self.name)
        if self.__validator.is_valid_column_name(column.name, self.__columns):
            self.__columns.update({column.name: column})
        else:
            raise ex.ColumnNameAlreadyInUseException(column.name)

