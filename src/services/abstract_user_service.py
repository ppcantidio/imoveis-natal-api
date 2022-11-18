from src.database import UserDB
from src.utils.errors import AbstractErrror

class AbstractUserService:
    def __init__(self, user_object):
        self.user_object = user_object
        self.db = UserDB()

    def create_user(self):
        if self.__user_existence():
            raise AbstractErrror('user alredy exist')

        

        

        

    def get_user(self):
        pass


    def __user_existence(self):
        if self.db.get_object_by_email(self.user.email):
            return True
        return False
