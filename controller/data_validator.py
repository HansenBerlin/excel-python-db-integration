from datetime import datetime
from models import column_model as cm, database as db
from common import data_types as dt


class DataValidator:
    def __init__(self, database: db):
        self.__database = database
        self.__validPairs = self.__create_valid_data_pairs()

    def is_valid_data_type(self, value):
        value_type = type(value)
        for k, v in self.__validPairs:
            if v == value_type and k == dt:
                return True
        return False

    def is_valid_foreign_key(self, ref_table: str, ref_col: str):
        for table in self.__database.tables:
            if table.name is ref_table:
                columns = table.get_columns_list()
                for col in columns:
                    if col.name is ref_col:
                        return True
        return False

    @staticmethod
    def is_valid_column_name(column_name: str, columns: dict[cm.ColumnModel]):
        for k in columns.keys():
            if k is column_name:
                return False
        return True

    @staticmethod
    def __create_valid_data_pairs():
        datatype = [type(str), type(float), type(int), type(datetime)]
        return {
            dt.DbDataTypes.VARCHAR: [datatype[0], datatype[1], datatype[2], datatype[3]],
            dt.DbDataTypes.DOUBLE: [datatype[1], datatype[2]],
            dt.DbDataTypes.INT: [datatype[2]],
            dt.DbDataTypes.DATETIME: [datatype[3]]
        }

