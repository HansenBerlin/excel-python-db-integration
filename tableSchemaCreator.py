import table_model as tm


class TableSchemaCreator:
    def __init__(self, file_to_write: str):
        self.__file = file_to_write

    def convert_to_file(self, table: tm, append: bool):
        m = (lambda : 'a' if append else 'w')()
        file = open(self.__file, m)
        content = self.__convert_in_string(table)
        file.write(content)
        file.close()
        print(content)

    def __convert_in_string(self, table: tm) -> str:
        base = f'GO \nCREATE TABLE {table.name} ('
        content = ''
        cols = table.get_columns_list()
        for col in cols:
            content += f'{col.name}{col.data_type}{col.is_pk}{col.not_null}{col.ref},'
        content = content[:-1]
        return f'{base}{content})\n'

