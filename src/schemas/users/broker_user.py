from marshmallow import fields

from src.schemas.users.abstract_user import AbstractUser


class BrokerUser(AbstractUser):
    creci = fields.String()
    url_profile_image = fields.String()