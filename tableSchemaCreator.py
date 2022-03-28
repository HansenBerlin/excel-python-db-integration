import table_model as tm


class TableSchemaCreator:
    def __init__(self, file_to_write: str):
        self.__file = file_to_write

    def convert_to_file(self, table: tm, append: bool):
        m = (lambda: 'a' if append else 'w')()
        file = open(self.__file, m)
        content = self.__concat_entities_to_string(table)
        file.write(content)
        file.close()
        print(content)

    @staticmethod
    def __concat_entities_to_string(table: tm) -> str:
        base = f'GO \nCREATE TABLE {table.name} ('
        content = ''
        cols = table.get_columns_list()
        for col in cols:
            content += f'{col.name}{col.data_type_text}{col.is_pk_text}{col.not_null_text}{col.ref_text}, '
        content = content[:-2]
        return f'{base}{content})\n'

