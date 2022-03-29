class ForeignKeyReferenceNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(f'The reference the given foreign key is pointing at could\'t be found. ({message})')


class DatatypeCastingException(Exception):
    def __init__(self, message='Value can\'t be casted to data type.'):
        super().__init__(message)


class ColumnNameAlreadyInUseException(Exception):
    def __init__(self, message):
        super().__init__(f'Column name {message} already in use in this table')


class TableNameAlreadyInUseException(Exception):
    def __init__(self, message='Table name already in use in this table'):
        super().__init__(message)


class RowAddingLockedException(Exception):
    def __init__(self, message):
        super().__init__(f'Datasets were already added to this table ({message}). Column adding is locked.')

