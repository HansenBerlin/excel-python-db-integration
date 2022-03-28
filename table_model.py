from copy import deepcopy
from dataValidator import DataValidator
import randomDataCreator as rN
import columnModel as cM
import databaseExceptions as eX


class TableModel:
    def __init__(self, table_name: str, validator: DataValidator):
        self.name = table_name
        self.__columns = dict()
        self.__validator = validator
        self.__is_row_adding_locked = False
        self.__rows = dict()
        self.__id_count = 0

    def add_column(self, column: cM):
        if self.__is_row_adding_locked:
            raise eX.RowAddingLockedException
        if self.__validator.is_valid_column_name(column.name, self.__columns):
            self.__columns.update({column.name: column})
        else:
            raise eX.ColumnNameAlreadyInUseException()

    def add_random_dataset(self):
        self.__is_row_adding_locked = True
        self.__id_count += 1
        for k, v in self.__columns.items():
            if v.is_pk:
                data = self.__id_count
            else:
                data = rN.RandomDataCreator.create_matching_random_data(v.data_type)
            self.__rows.update({k: data})

    def get_columns_list(self):
        ls = []
        for v in self.__columns.values():
            ls.append(deepcopy(v))
        return ls

    def get_rows_list(self):
        return deepcopy(self.__rows)

