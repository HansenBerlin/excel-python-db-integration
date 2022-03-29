import json
import random as r
import value_objects as vo
import data_types as dt
from datetime import datetime


class RandomDataCreator:
    def __init__(self, path_to_config_file: str):
        file = open(path_to_config_file)
        config = json.load(file)
        time = config['Event']['StartAfterDate']
        self.__start_event_after = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        self.__end_event_before = datetime.strptime(config['Event']['EndAfterDate'], '%Y-%m-%d %H:%M:%S.%f')
        self.__start_bday_after = datetime.strptime(config['BirthdayRange']['AfterDate'], '%Y-%m-%d %H:%M:%S.%f')
        self.__end_bday_before = datetime.strptime(config['BirthdayRange']['BeforeDate'], '%Y-%m-%d %H:%M:%S.%f')
        self.__path_first_names = config['PathToNameFiles']['FemaleFirstNames']
        self.__path_last_names = config['PathToNameFiles']['FemaleLastNames']

    def create_matching_random_data(self, data_type: dt, datasets_count: int = 100):
        if data_type is dt.DbDataTypes.INT:
            return r.randrange(1, datasets_count)
        if data_type is dt.DbDataTypes.VARCHAR:
            return f"'{r.choice(vo.names)}'"
        if data_type is dt.DbDataTypes.DATETIME:
            date_time = self.__generate_random_date_in_range()
            date_time = date_time.strftime("%Y-%m-%d %H:%M:%S")
            return f"cast(N'{date_time}' AS DATETIME)"
        if data_type is dt.DbDataTypes.DOUBLE:
            return r.random()

    def create_matching_random_data2(self, rand_data_type: dt.RandomDataTypes, datasets_count: int = 100):
        if rand_data_type is dt.RandomDataTypes.ID:
            return r.randrange(1, datasets_count)
        if rand_data_type is dt.RandomDataTypes.FEMALEFIRSTNAME or dt.RandomDataTypes.FEMALELASTNAME:
            return self.__generate_random_name(rand_data_type)
        if rand_data_type is dt.RandomDataTypes.BIRTHDATE or dt.RandomDataTypes.EVENTSTARTTIME:
            date_time = self.__generate_random_date_in_range(rand_data_type)
            date_time = date_time.strftime("%Y-%m-%d %H:%M:%S")
            return f"cast(N'{date_time}' AS DATETIME)"
        if rand_data_type is dt.RandomDataTypes.RUNINSECONDS:
            return r.random()

    def __generate_random_date_in_range(self, rand_data_type: dt.RandomDataTypes):
        if dt.RandomDataTypes is dt.RandomDataTypes.BIRTHDATE:
            start = self.__start_bday_after
            end = self.__end_bday_before
        else:
            start = self.__start_event_after
            end = self.__end_event_before
        return start + (end - start) * r.random()

    def __generate_random_name(self, rand_data_type: dt.RandomDataTypes):
        if rand_data_type is dt.RandomDataTypes.FEMALEFIRSTNAME:
            file = open(self.__path_first_names)
        else:
            file = open(self.__path_last_names)
        names = json.load(file)
        return r.choice(names)


