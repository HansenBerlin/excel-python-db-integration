import dataTypes as dT
from copy import deepcopy


class ColumnModel:
    def __init__(self, col_name: str, data_type: dT, is_pk: bool = False, not_null: bool = True,
                 is_fk: bool = False, ref_table: str = '', ref_col: str = ''):
        self.name = f' {col_name}'
        self.data_type = f' {data_type.value}'
        self.is_pk = (lambda: ' PRIMARY KEY' if is_pk else '')()
        self.not_null = (lambda: ' NOT NULL' if not_null else '')()
        self.is_fk = (lambda: ' FOREIGN KEY' if is_fk else '')()
        self.ref = (lambda: f' REFERENCES {ref_table}({ref_col})' if is_fk else '')()

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result
