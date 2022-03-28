import table_model as tm


class TableSchemaCreator:
    def __init__(self, file_to_write: str):
        self.__file = file_to_write

    def create_table_schema_in_file(self, table: tm, append: bool):
        m = (lambda: 'a' if append else 'w')()
        file = open(self.__file, m)
        tables = self.__concat_createtable_entities_to_string(table)
        values = self.__concat_insert_entities_to_string(table)
        file.write(tables + values)
        file.close()

    @staticmethod
    def __concat_createtable_entities_to_string(table: tm) -> str:
        base = f'\nCREATE TABLE {table.schema}.{table.name} ('
        content = ''
        cols = table.get_columns_list()
        for col in cols:
            content += f'{col.name}{col.data_type_text}{col.is_pk_text}{col.not_null_text}{col.ref_text}, '
        content = content[:-2]
        content = content.replace('<parenttablename>', table.name)
        return f'{base}{content})\nGO'

    @staticmethod
    def __concat_insert_entities_to_string(table: tm) -> str:
        cn_insert = ''
        cols = table.get_columns_list()
        for col in cols:
            cn_insert += f'{col.name}, '
        cn_insert = cn_insert[:-2]

        rows = table.get_rows_dict()
        cn_values = ''
        for row in rows:
            cn_temp = ''
            for val in row:
                cn_temp += f'{val}, '
            cn_temp = cn_temp[:-2]
            cn_values += f'({cn_temp}), '
        cn_values = cn_values[:-2]

        return f'\nINSERT INTO {table.schema}.{table.name} ({cn_insert}) VALUES {cn_values}\nGO'
