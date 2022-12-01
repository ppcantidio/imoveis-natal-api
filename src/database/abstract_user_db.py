from src.database.database import ConnectionDB


class AbstractUserDB:
    def __init__(self, collection):
        self.connection = ConnectionDB.get_connection(collection)
