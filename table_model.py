from copy import deepcopy
from data_validator import DataValidator
import column_model as cm
import database_exceptions as eX
from random_data_creator import RandomDataCreator


class TableModel:
    def __init__(self, random_data_gen: RandomDataCreator, table_name: str, schema_name: str = '',
                 validator: DataValidator = DataValidator()):
        self.name = table_name
        self.schema = schema_name
        self.__columns = {}
        self.__is_col_adding_locked = False
        self.__rows = []
        self.__id_count = 0
        self.__validator = validator
        self.__rnd_gen = random_data_gen

    def add_columns(self, columns: list[cm]):
        for col in columns:
            self.__add_column(col)

    def add_random_datasets(self, datasets_count: int):
        self.__is_col_adding_locked = True
        for i in range(datasets_count):
            self.__id_count += 1
            data_set = []
            for k, v in self.__columns.items():
                if v.is_pk:
                    data = self.__id_count
                elif v.is_fk:
                    data = self.__rnd_gen.create_matching_random_data(v.data_type, v.fk_model.ref_count)
                else:
                    data = self.__rnd_gen.create_matching_random_data2(v.rand_data_info, datasets_count)
                data_set.append(data)
            self.__rows.append(data_set)

    def get_columns_list(self):
        ls = []
        for v in self.__columns.values():
            ls.append(deepcopy(v))
        return ls

    def get_rows_dict(self):
        return deepcopy(self.__rows)

    def __add_column(self, column: cm):
        if self.__is_col_adding_locked:
            raise eX.RowAddingLockedException
        if self.__validator.is_valid_column_name(column.name, self.__columns):
            self.__columns.update({column.name: column})
        else:
            raise eX.ColumnNameAlreadyInUseException()
