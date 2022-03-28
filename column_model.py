import dataTypes as dT


class ColumnModel:
    def __init__(self, col_name: str, data_type: dT, is_fk: bool, is_pk: bool, constraint: str, not_null: bool):
        self.is_fk = is_fk
        self.is_pk = is_pk
        self.col_name = col_name
        self.data_type = data_type
        self.constraint = constraint
        self.not_null = not_null


