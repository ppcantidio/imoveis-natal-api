from src.database.database import Database
import pymongo


class AbstractUserDB(Database):
    def get_user_by_email(self, email):
        where = {"email": email}
        result = self.collection.find_one(where)
        self._change_uuid_type(result)
        return result

    def get_user_by_cpf(self, cpf):
        where = {"cpf": cpf}
        result = self.collection.find_one(where)
        self._change_uuid_type(result)
        return result

    def get_user_celular(self, celular):
        where = {"celular": celular}
        result = self.collection.find_one(where)
        self._change_uuid_type(result)
        return result
