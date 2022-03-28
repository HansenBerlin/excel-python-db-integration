from copy import deepcopy
import column_model as cm


class TableModel:
    def __init__(self, table_name):
        self.name = table_name
        self.columns = dict()

    def add_column(self, column: cm):
        self.columns.update({column.name: column})

    def get_columns_list(self):
        ls = []
        for v in self.columns.values():
            ls.append(deepcopy(v))
        return ls
