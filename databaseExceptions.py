class ForeignKeyReferenceNotFoundException(Exception):
    def __init__(self, message='The reference the given foreign key is pointing at could\'t be found.'):
        super().__init__(message)


class DatatypeCastingException(Exception):
    def __init__(self, message='Value can\'t be casted to data type.'):
        super().__init__(message)


class ColumnNameAlreadyInUseException(Exception):
    def __init__(self, message='Column name already in use in this table'):
        super().__init__(message)


class TableNameAlreadyInUseException(Exception):
    def __init__(self, message='Table name already in use in this table'):
        super().__init__(message)


class RowAddingLockedException(Exception):
    def __init__(self, message='Datasets were already added to this table. Column adding is locked.'):
        super().__init__(message)

