from marshmallow import fields

from src.schemas.users.abstract_user import AbstractUser


class BrokerSchema(AbstractUser):
    creci = fields.String(required=True)
