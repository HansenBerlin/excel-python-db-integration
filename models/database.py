class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.tables = []
        return cls._instance

    def add_table(self, table):
        self.tables.append(table)

