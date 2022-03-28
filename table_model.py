import column_model as cm


class TableModel:
    def __init__(self, table_name):
        self.table_name = table_name
        self.__columns = {}

    def add_column(self, column: cm):
        self.__columns[column.col_name] = column

    def get_column(self):
        return len(self.__columns)
