from common import data_types as dt
from copy import deepcopy

from models.foreign_key_model import ForeignKeyModel


class ColumnModel:
    def __init__(self, col_name: str, data_type: dt, rand_data_info: dt.RandomDataTypes, is_pk: bool = False,
                 not_null: bool = True, is_fk: bool = False, fk_model: ForeignKeyModel = None):
        self.name = col_name
        self.data_type = data_type
        self.rand_data_info = rand_data_info
        self.is_pk = is_pk
        self.is_fk = is_fk
        self.data_type_text = f' {data_type.value}'
        self.is_pk_text = (lambda: ' PRIMARY KEY' if is_pk else '')()
        self.not_null_text = (lambda: ' NOT NULL' if not_null else '')()
        self.is_fk_text = (lambda: ' FOREIGN KEY' if is_fk else '')()
        self.ref_text = (lambda: f' CONSTRAINT <parenttablename>_{fk_model.ref_table}_{fk_model.ref_col}_fk '
                                 f'REFERENCES {fk_model.ref_schema}.{fk_model.ref_table}' if is_fk else '')()
        self.fk_model = fk_model

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result
