from models import table_model as tm, database_model_singleton as db
import common.value_objects as vo


class TableSchemaCreator:
    def __init__(self, db_name: str, schema_name: str, database: db):
        self.__file = f'create-database.sql'
        self.__db_name = db_name
        self.__db = database
        self.__schema_name = schema_name

    def create_table_schema_in_file(self):
        file = open(self.__file, 'w')
        dbsetup = self.__create_entry_script()
        file.write(dbsetup)
        tables, values = '', ''
        for table in self.__db.tables:
            table.remove_duplicates()
            tables += self.__concat_createtable_entities_to_string(table)
            values += self.__concat_insert_entities_to_string(table)
        file.write(tables + values)
        file.close()

    def __create_entry_script(self):
        content = ''
        tables = self.__db.tables
        tables.reverse()
        for table in tables:
            temp = vo.table_clear
            temp = temp.replace(vo.table_name_placeholder, table.name)
            content += temp
        tables.reverse()
        #content += vo.schema_init
        content += vo.db_init
        content = content.replace(vo.schema_name_placeholder, self.__schema_name)
        content = content.replace(vo.db_name_placeholder, self.__db_name)
        return content

    @staticmethod
    def __concat_createtable_entities_to_string(table: tm):
        base = f'\nCREATE TABLE {table.schema}{table.name} ('
        content = ''
        cols = table.get_columns_list()
        for col in cols:
            content += f'{col.name}{col.data_type_text}{col.is_pk_text}{col.not_null_text}{col.ref_text}, '
        content = content[:-2]
        content = content.replace(vo.parent_table_name_placeholder, table.name)
        return f'{base}{content})\nGO'

    @staticmethod
    def __concat_insert_entities_to_string(table: tm):
        cn_insert = ''
        cols = table.get_columns_list()
        for col in cols:
            cn_insert += f'{col.name}, '
        cn_insert = cn_insert[:-2]
        rows = table.get_rows_dict()
        cn_values = '\n'
        for row in rows:
            cn_temp = ''
            for val in row:
                cn_temp += f'{val}, '
            cn_temp = cn_temp[:-2]
            cn_values += f'({cn_temp}),\n'
        cn_values = cn_values[:-2]
        return f'\nINSERT INTO {table.schema}{table.name} ({cn_insert}) VALUES {cn_values}\nGO'





