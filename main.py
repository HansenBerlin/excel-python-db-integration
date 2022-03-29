import json
from common import data_types as dt
from controller.data_validator import DataValidator
from models.column_model import ColumnModel
from models.database import Database
from models.foreign_key_model import ForeignKeyModel
from controller.random_data_creator import RandomDataCreator
from controller.table_schema_creator import TableSchemaCreator
from models.table_model import TableModel

config_file_path = './data/randomGeneratorConfig.json'
file = open(config_file_path)
config = json.load(file)
db_name = config['DatabaseInfo']['Name']
schema_name = config['DatabaseInfo']['Schema']

database = Database()
validator = DataValidator(database)
rnd_creator = RandomDataCreator(config_file_path)

team_datasets = 10
athlete_datasets = 100
boats_datasets = 20

teams = TableModel(rnd_creator, validator, 'teams', schema_name)
team_id = ColumnModel('id', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, True)
team_name = ColumnModel('name', dt.DbDataTypes.VARCHAR, dt.RandomDataTypes.SPORTSTEAM)
team_member_count = ColumnModel('member_count', dt.DbDataTypes.INT, dt.RandomDataTypes.MEMBERCOUNT)
teams.add_columns([team_id, team_name, team_member_count])
teams.add_random_datasets(team_datasets)

athletes = TableModel(rnd_creator, validator, 'athletes', schema_name)
athlete_id = ColumnModel('id', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, True)
athlete_firstname = ColumnModel('firstname', dt.DbDataTypes.VARCHAR, dt.RandomDataTypes.FEMALEFIRSTNAME)
athlete_surname = ColumnModel('surname', dt.DbDataTypes.VARCHAR, dt.RandomDataTypes.FEMALELASTNAME)
athlete_birthday = ColumnModel('birth_date', dt.DbDataTypes.DATETIME, dt.RandomDataTypes.BIRTHDATE)
athlete_fk_model = ForeignKeyModel(team_datasets, 'teams', 'id', schema_name)
athlete_sportsteam_fk = ColumnModel('team_fk', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, False, False, True, athlete_fk_model)
athletes.add_columns([athlete_id, athlete_firstname, athlete_surname, athlete_birthday, athlete_sportsteam_fk])
athletes.add_random_datasets(athlete_datasets)

boats = TableModel(rnd_creator, validator, 'boats', schema_name)
boats_id = ColumnModel('id', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, True)
boats_name = ColumnModel('name', dt.DbDataTypes.VARCHAR, dt.RandomDataTypes.BOATNAME)
boats_fk_model = ForeignKeyModel(athlete_datasets, 'athletes', 'id', schema_name)
boats_athlete_fk = ColumnModel('batswoman_fk', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, False, False, True, boats_fk_model)
boats_seats = ColumnModel('seats', dt.DbDataTypes.INT, dt.RandomDataTypes.SEATS)
boats.add_columns([boats_id, boats_name, boats_athlete_fk, boats_seats])
boats.add_random_datasets(boats_datasets)

athletes_in_boat = TableModel(rnd_creator, validator, 'athletes_in_boat', schema_name, True)
athletes_in_boat_fk_model_athlete = ForeignKeyModel(athlete_datasets, 'athletes', 'id', schema_name)
athletes_in_boat_fk_model_boat = ForeignKeyModel(boats_datasets, 'boats', 'id', schema_name)
athletes_in_boat_athlete_fk = ColumnModel('athlete_fk', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, False, False, True,
                                          athletes_in_boat_fk_model_athlete)
athletes_in_boat_boat_fk = ColumnModel('boat_fk', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, False, False, True,
                                       athletes_in_boat_fk_model_boat)
athletes_in_boat.add_columns([athletes_in_boat_athlete_fk, athletes_in_boat_boat_fk])
athletes_in_boat.add_random_datasets(500)


creator = TableSchemaCreator(db_name, schema_name, database)
creator.create_table_schema_in_file()


