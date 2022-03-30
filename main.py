import json
import subprocess
from pathlib import Path
from common import data_types as dt
from controller.data_validator import DataValidator
from models.column_model import ColumnModel
from models.database_model_singleton import DatabaseModelSingleton
from models.foreign_key_model import ForeignKeyModel
from controller.random_data_creator import RandomDataCreator
from controller.table_schema_creator import TableSchemaCreator
from models.table_model import TableModel

p = Path(__file__)
dir_abs = p.parent.absolute()
config_file_path = f'{dir_abs}\\data\\'
file = open(config_file_path + 'randomGeneratorConfig.json')
config = json.load(file)
db_name = config['DatabaseInfo']['Name']
schema_name = config['DatabaseInfo']['Schema']

database = DatabaseModelSingleton()
validator = DataValidator(database)
rnd_creator = RandomDataCreator(config_file_path)

team_datasets = 10
athlete_datasets = 60
boats_datasets = 20
training_events_datasets = 100


teams_fk_model = ForeignKeyModel(team_datasets, 'teams', 'id', schema_name)
athletes_fk_model = ForeignKeyModel(athlete_datasets, 'athletes', 'id', schema_name)
boats_fk_model = ForeignKeyModel(boats_datasets, 'boats', 'id', schema_name)
training_events_fk_model = ForeignKeyModel(training_events_datasets, 'training_events', 'id', schema_name)


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
athlete_sportsteam_fk = ColumnModel('team_fk', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, False, None, False, True, teams_fk_model)
athletes.add_columns([athlete_id, athlete_firstname, athlete_surname, athlete_birthday, athlete_sportsteam_fk])
athletes.add_random_datasets(athlete_datasets)


boats = TableModel(rnd_creator, validator, 'boats', schema_name)
boats_id = ColumnModel('id', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, True)
boats_name = ColumnModel('name', dt.DbDataTypes.VARCHAR, dt.RandomDataTypes.BOATNAME)
boats_athlete_fk = ColumnModel('batswoman_fk', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, False, None, False, True, athletes_fk_model)
boats_seats = ColumnModel('seats', dt.DbDataTypes.INT, dt.RandomDataTypes.SEATS)
boats.add_columns([boats_id, boats_name, boats_athlete_fk, boats_seats])
boats.add_random_datasets(boats_datasets)


athletes_in_boat = TableModel(rnd_creator, validator, 'athletes_in_boat', schema_name, True)
athletes_in_boat_athlete_fk = ColumnModel('athlete_fk', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, False, None, False, True, athletes_fk_model)
athletes_in_boat_boat_fk = ColumnModel('boat_fk', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, False, 5, False, True, boats_fk_model)
athletes_in_boat.add_columns([athletes_in_boat_athlete_fk, athletes_in_boat_boat_fk])
athletes_in_boat.add_random_datasets(athlete_datasets * 2)


training_events = TableModel(rnd_creator, validator, 'training_events', schema_name)
training_events_id = ColumnModel('id', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, True)
training_events_starttime = ColumnModel('starttime', dt.DbDataTypes.DATETIME, dt.RandomDataTypes.EVENTSTARTTIME, False, None, False)
training_events.add_columns([training_events_id, training_events_starttime])
training_events.add_random_datasets(training_events_datasets)


training_event_results = TableModel(rnd_creator, validator, 'training_event_results', schema_name)
training_event_results_id = ColumnModel('id', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, True)
training_event_results_finish_time = ColumnModel('result', dt.DbDataTypes.DOUBLE, dt.RandomDataTypes.RUNINSECONDS)
training_event_results_boat_fk = ColumnModel('boat_fk', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, False, None, False, True, boats_fk_model)
training_event_results_events_fk = ColumnModel('training_events_fk', dt.DbDataTypes.INT, dt.RandomDataTypes.ID, False, 5, False, True, training_events_fk_model)
training_event_results.add_columns([training_event_results_id, training_event_results_finish_time, training_event_results_boat_fk, training_event_results_events_fk])
training_event_results.add_random_datasets(training_events_datasets * 10)


creator = TableSchemaCreator(db_name, schema_name, database)
creator.create_table_schema_in_file()


return_code = subprocess.call('cd out', shell=True)
if return_code == 0:
    return_code = subprocess.call('dir', shell=True)
    return_code = subprocess.call('docker build -t db-demo .', shell=True)
if return_code == 0:
    return_code = subprocess.call('docker run -p 1000:1433 -d db-demo', shell=True)
