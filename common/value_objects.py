db_init = 'DROP DATABASE IF EXISTS <db_name>\nGO\nCREATE DATABASE <db_name>\nGO\nUSE <db_name>\nGO\n'
table_clear = 'DROP TABLE IF EXISTS <schema_name><table_name>\nGO\n'
schema_init = 'DROP SCHEMA IF EXISTS <schema_name>\nGO\nCREATE SCHEMA <schema_name>\nGO\n'
db_name_placeholder = '<db_name>'
table_name_placeholder = '<table_name>'
schema_name_placeholder = '<schema_name>'
parent_table_name_placeholder = '<parenttablename>'

boat_names = ['Albatros', 'Arche Noah', 'Bananenfrachter', 'Bin Baden', 'Discovery', 'Endeavour', 'H2O Breaker',
              'Ilayda ', 'Juan', 'Kahla', 'Neyle', 'Titanic', 'Pomposa', 'Scrootoh', 'Udine', 'Ver Boot', 'Waterloo',
              'Albatros 2', 'Arche Noah 2', 'Bananenfrachter 2', 'Bin Baden 2', 'Discovery 2', 'Endeavour 2',
              'H2O Breaker 2', 'Ilayda 2', 'Juan 2', 'Kahla 2', 'Neyle 2', 'Titanic 2', 'Pomposa 2', 'Scrootoh 2',
              'Udine 2', 'Ver Boot 2', 'Waterloo 2']

sportsteam_names = ['SV Bremen', 'SV Hamburg Nord', 'SV Unterhachingen', 'RC Tiefsee', 'RC Oberspree', 'RV Borkum',
                    'RV Kassel Ost', 'SV Abgesoffen', 'RC Engine-Less', 'SV Red Bull Bonn', 'SV Bremen 2',
                    'SV Hamburg Nord 2', 'SV Unterhachingen 2', 'RC Tiefsee 2', 'RC Oberspree 2', 'RV Borkum 2',
                    'RV Kassel Ost 2', 'SV Abgesoffen 2', 'RC Engine-Less 2', 'SV Red Bull Bonn 2', 'SV Bremen 3',
                    'SV Hamburg Nord 3', 'SV Unterhachingen 3', 'RC Tiefsee 3', 'RC Oberspree 3', 'RV Borkum 3',
                    'RV Kassel Ost 3', 'SV Abgesoffen 3', 'RC Engine-Less 3', 'SV Red Bull Bonn 3']
