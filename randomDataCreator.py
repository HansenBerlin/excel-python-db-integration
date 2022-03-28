import dataTypes as dT
import datetime as date


class RandomDataCreator:

    @staticmethod
    def create_matching_random_data(data_type: dT):
        if data_type is dT.DataTypes.INT:
            return 1
        if data_type is dT.DataTypes.VARCHAR:
            return 'hello'
        if data_type is dT.DataTypes.DATETIME:
            return date.datetime.now()
        if data_type is dT.DataTypes.DOUBLE:
            return 1.4
