import dataTypes as dT
from column_model import ColumnModel
from dataValidator import DataValidator
from foreign_key_model import ForeignKeyModel
from randomDataCreator import RandomDataCreator
from tableSchemaCreator import TableSchemaCreator
from table_model import TableModel

rnd_creator = RandomDataCreator()

col_one = ColumnModel('ID', dT.DataTypes.INT, True)
col_two = ColumnModel('name', dT.DataTypes.VARCHAR)
table1 = TableModel(rnd_creator, 'person', 'test')
table1.add_columns([col_one, col_two])

col_one_x = ColumnModel('ID', dT.DataTypes.INT, True)
col_two_x = ColumnModel('time', dT.DataTypes.DOUBLE)
fk_model = ForeignKeyModel(10, 'person', 'ID', 'test')
col_three_x = ColumnModel('person_fk', dT.DataTypes.INT, False, False, True, fk_model)
table2 = TableModel(rnd_creator, 'time', 'test')
table2.add_columns([col_one_x, col_two_x, col_three_x])

col_one_y = ColumnModel('ID', dT.DataTypes.INT, True)
col_two_y = ColumnModel('start_time', dT.DataTypes.DATETIME)
fk_model2 = ForeignKeyModel(50, 'time', 'ID', 'test')
col_three_y = ColumnModel('time_fk', dT.DataTypes.INT, False, False, True, fk_model2)
table3 = TableModel(rnd_creator, 'startdates', 'test')
table3.add_columns([col_one_y, col_two_y, col_three_y])

table1.add_random_datasets(10)
table2.add_random_datasets(50)
table3.add_random_datasets(500)

creator = TableSchemaCreator('testfile.txt')
creator.create_table_schema_in_file(table1, False)
creator.create_table_schema_in_file(table2, True)
creator.create_table_schema_in_file(table3, True)



