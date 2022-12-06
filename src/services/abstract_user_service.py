from src.database.abstract_user_db import AbstractUserDB
from src.utils.errors_util import CommonError


class AbstractUserService:
    def __init__(self, collection_name):
        self.collection_name = collection_name
        self.db = AbstractUserDB(self.collection_name)

    def create_user(self, user_object):
        self._check_user_existence(user_object)

        user_object["senha"] = self._generate_password_hash(user_object)

        self.db.insert_object(user_object)

    def get_user(self, user_uuid):
        user = self.db.get_object_by_uuid(user_uuid)
        if user is None:
            raise CommonError("Usuario não encontrado")
        del user["senha"]
        return user

    def _check_user_existence(self, user_object):
        if self.db.get_user_by_email(user_object.get("email")):
            raise CommonError("Já existe um usuario cadastrado com esse email", 400)
        elif self.db.get_user_by_cpf(user_object.get("cpf")):
            raise CommonError("Já existe um usuario cadastrado com esse cpf", 400)
        elif self.db.get_user_celular(user_object.get("celular")):
            raise CommonError("Já existe um usuario cadastrado com esse numero de celular", 400)

    def _generate_password_hash(self, user_object):
        return user_object.get("senha")
