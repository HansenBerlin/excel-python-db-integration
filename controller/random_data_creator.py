import json
import random as r
import common.data_types as dt
import common.value_objects as vo
from datetime import datetime


class RandomDataCreator:
    def __init__(self, path_to_config_file: str):
        file = open(path_to_config_file + 'randomGeneratorConfig.json')
        config = json.load(file)
        self.__start_event_after = datetime.strptime(config['Event']['StartAfterDate'], '%Y-%m-%d %H:%M:%S')
        self.__end_event_before = datetime.strptime(config['Event']['EndBeforeDate'], '%Y-%m-%d %H:%M:%S')
        self.__start_bday_after = datetime.strptime(config['BirthdayRange']['AfterDate'], '%Y-%m-%d')
        self.__end_bday_before = datetime.strptime(config['BirthdayRange']['BeforeDate'], '%Y-%m-%d')
        self.__path_first_names = f'{path_to_config_file}\\' + config['PathToNameFiles']['FemaleFirstNames']
        self.__path_last_names = f'{path_to_config_file}\\' + config['PathToNameFiles']['FemaleLastNames']
        self.__run_seconds_min_five_people = config['TimeRangeForRuns']['BoatWithFivePeople']['MinTimeInSecs']
        self.__run_seconds_max_five_people = config['TimeRangeForRuns']['BoatWithFivePeople']['MaxTimeInSecs']

    def create_matching_random_data(self, rand_data_type: dt.RandomDataTypes, datasets_count: int = 100):
        if rand_data_type is dt.RandomDataTypes.RUNINSECONDS:
            time = self.__generate_random_time_for_run()
            return round(time, 3)
        elif rand_data_type is dt.RandomDataTypes.EVENTSTARTTIME:
            date_time = self.__generate_random_date_in_range(rand_data_type)
            date_time = date_time.strftime("%Y-%m-%d %H:%M:%S")
            return f"cast(N'{date_time}' AS DATETIME)"
        elif rand_data_type is dt.RandomDataTypes.BIRTHDATE:
            date_time = self.__generate_random_date_in_range(rand_data_type)
            date_time = date_time.strftime("%Y-%m-%d")
            return f"cast(N'{date_time}' AS DATETIME)"
        elif rand_data_type is dt.RandomDataTypes.ID:
            return r.randrange(1, datasets_count)
        elif rand_data_type is dt.RandomDataTypes.MEMBERCOUNT:
            return r.randrange(50, 2000)
        elif rand_data_type is dt.RandomDataTypes.SEATS:
            return r.randrange(5, 6)
        elif rand_data_type is dt.RandomDataTypes.DISTANCEINMETERS:
            return 1000
        elif rand_data_type is dt.RandomDataTypes.FEMALEFIRSTNAME \
                or rand_data_type is dt.RandomDataTypes.FEMALELASTNAME:
            return f"'{self.__generate_random_name(rand_data_type)}'"
        elif rand_data_type is dt.RandomDataTypes.SPORTSTEAM:
            team = r.choice(vo.sportsteam_names)
            vo.sportsteam_names.remove(team)
            return f"'{team}'"
        elif rand_data_type is dt.RandomDataTypes.BOATNAME:
            name = r.choice(vo.boat_names)
            vo.boat_names.remove(name)
            return f"'{name}'"

    def __generate_random_date_in_range(self, rand_data_type: dt.RandomDataTypes):
        if rand_data_type is dt.RandomDataTypes.BIRTHDATE:
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

    def __generate_random_time_for_run(self):
        return r.uniform(self.__run_seconds_min_five_people, self.__run_seconds_max_five_people)


