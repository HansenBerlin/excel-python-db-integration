from datetime import datetime
import column_model as cm
import data_types as dT


class DataValidator:
    def __init__(self):
        self.__validPairs = self.__create_valid_data_pairs()

    def is_valid_data_type(self, value):
        value_type = type(value)
        for k, v in self.__validPairs:
            if v == value_type and k == dT:
                return True
        return False

    @staticmethod
    def is_valid_foreign_key(column: cm, tables):
        for col in tables:
            if col.name is column.name:
                return True
        return False

    @staticmethod
    def is_valid_column_name(column_name: str, columns):
        for k in columns.keys():
            if k is column_name:
                return False
        return True

    @staticmethod
    def __create_valid_data_pairs():
        dt = [type(str), type(float), type(int), type(datetime)]
        return {
            dT.DbDataTypes.VARCHAR: [dt[0], dt[1], dt[2], dt[3]],
            dT.DbDataTypes.DOUBLE: [dt[1], dt[2]],
            dT.DbDataTypes.INT: [dt[2]],
            dT.DbDataTypes.DATETIME: [dt[3]]
        }

