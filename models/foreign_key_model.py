
class ForeignKeyModel:
    def __init__(self, ref_count: int, ref_table: str, ref_col: str, ref_schema: str = ''):
        self.ref_count = ref_count
        self.ref_table = ref_table
        self.ref_col = ref_col
        self.ref_schema = ref_schema
