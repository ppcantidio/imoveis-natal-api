from src.services.abstract_user_service import AbstractUserService
from src.database.abstract_user_db import AbstractUserDB


class BrokerService(AbstractUserService):
    def __init__(self):
        self.collection_name = "broker"
        self.db = AbstractUserDB(self.collection_name)
