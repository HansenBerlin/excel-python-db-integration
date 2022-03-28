import random as r
import value_objects as vo
import data_types as dT
from datetime import datetime


class RandomDataCreator:
    def __init__(self, start_date=datetime(2023, 6, 1, 00, 00, 00), end_date=datetime(2023, 6, 13, 00, 00, 00)):
        self.__start = start_date
        self.__end = end_date

    def create_matching_random_data(self, data_type: dT, datasets_count: int = 100):
        if data_type is dT.DataTypes.INT:
            return r.randrange(1, datasets_count)
        if data_type is dT.DataTypes.VARCHAR:
            return f"'{vo.names[r.randrange(0, 4)]}'"
        if data_type is dT.DataTypes.DATETIME:
            date_time = self.__generate_random_date_in_range()
            date_time = date_time.strftime("%Y-%m-%d %H:%M:%S")
            return f"cast(N'{date_time}' AS DATETIME)"
        if data_type is dT.DataTypes.DOUBLE:
            return r.random()

    @staticmethod
    def __generate_random_date_in_range():
        start = datetime(2023, 6, 1, 00, 00, 00)
        end = datetime(2023, 6, 13, 00, 00, 00)
        return start + (end - start) * r.random()
