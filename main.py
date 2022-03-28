import dataTypes as dT
from column_model import ColumnModel
from tableSchemaCreator import TableSchemaCreator
from table_model import TableModel

col_one = ColumnModel('ID', dT.DataTypes.INT, True)
col_two = ColumnModel('name', dT.DataTypes.VARCHAR, False)
table1 = TableModel('test.person')
table1.add_column(col_one)
table1.add_column(col_two)

col_one_x = ColumnModel('ID', dT.DataTypes.INT, True)
col_two_x = ColumnModel('value', dT.DataTypes.DATETIME)
col_three_x = ColumnModel('person_fk', dT.DataTypes.INT, False, False, True, 'test.person', 'ID')
table2 = TableModel('test.time')
table2.add_column(col_one_x)
table2.add_column(col_two_x)
table2.add_column(col_three_x)

creator = TableSchemaCreator('testfile.txt')
creator.convert_to_file(table1, False)
creator.convert_to_file(table2, True)

