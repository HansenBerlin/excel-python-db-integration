import json
import random
import data_types as dt
from column_model import ColumnModel
from foreign_key_model import ForeignKeyModel
from random_data_creator import RandomDataCreator
from table_schema_creator import TableSchemaCreator
from table_model import TableModel

rnd_creator = RandomDataCreator('randomGeneratorConfig.json')

col_one = ColumnModel('ID', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, True)
col_two = ColumnModel('first_name', dt.DbDataTypes.VARCHAR, dt.RandomDataTypes.FEMALEFIRSTNAME)
col_three = ColumnModel('last_name', dt.DbDataTypes.VARCHAR, dt.RandomDataTypes.FEMALELASTNAME)
col_four = ColumnModel('birthday', dt.DbDataTypes.DATETIME, dt.RandomDataTypes.BIRTHDATE)
table1 = TableModel(rnd_creator, 'person', 'test')
table1.add_columns([col_one, col_two, col_three])

col_one_x = ColumnModel('ID', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, True)
col_two_x = ColumnModel('time', dt.DbDataTypes.DOUBLE, dt.RandomDataTypes.RUNINSECONDS)
fk_model = ForeignKeyModel(10, 'person', 'ID', 'test')
col_three_x = ColumnModel('person_fk', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, False, False, True, fk_model)
table2 = TableModel(rnd_creator, 'time', 'test')
table2.add_columns([col_one_x, col_two_x, col_three_x])

col_one_y = ColumnModel('ID', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, True)
col_two_y = ColumnModel('start_time', dt.DbDataTypes.DATETIME, dt.RandomDataTypes.EVENTSTARTTIME)
fk_model2 = ForeignKeyModel(50, 'time', 'ID', 'test')
col_three_y = ColumnModel('time_fk', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, False, False, True, fk_model2)
table3 = TableModel(rnd_creator, 'startdates', 'test')
table3.add_columns([col_one_y, col_two_y, col_three_y])

table1.add_random_datasets(10)
table2.add_random_datasets(50)
table3.add_random_datasets(1000)

creator = TableSchemaCreator('testfile.txt')
creator.create_table_schema_in_file(table1, False)
creator.create_table_schema_in_file(table2, True)
creator.create_table_schema_in_file(table3, True)

