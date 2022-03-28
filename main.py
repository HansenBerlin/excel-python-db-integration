import dataTypes as dT
from column_model import ColumnModel
from table_model import TableModel

col_one = ColumnModel('name1', dT.DataTypes.TEXT, True, True, 'none', False)
col_two = ColumnModel('name2', dT.DataTypes.TEXT, True, True, 'none', False)
table1 = TableModel('tableOne')
table1.add_column(col_one)
table1.add_column(col_two)
print(table1.get_column())

