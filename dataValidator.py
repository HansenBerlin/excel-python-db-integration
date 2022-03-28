import dataTypes as dT


def translate_to_type(value, validate_type: dT):
    value_type = type(value)
    for k, v in __validPairs:
        if v == value_type and k == dT:
            return True
    return False


__validPairs = {
    dT.DataTypes.TEXT: type(str),
    dT.DataTypes.INT: type(int)
}
