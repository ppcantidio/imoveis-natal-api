from src.database import UserDB
from src.utils.errors_util import CommonError


class AbstractUserService:
    def __init__(self, user_db):
        self.db = user_db

    def create_user(self, user_object):
        self.__check_user_existence(user_object)

        user_object.password = self.__generate_password_hash(user_object)

        self.db.register_user(user_object)

    def get_user(self, user_id):
        user = self.db.get_user_by_id(user_id)
        return user

    def __check_user_existence(self, user_object):
        if self.db.get_object_by_email(user_object.email):
            raise CommonError("user alredy exist")

    def __generate_password_hash(self, user_object):
        return user_object.password
