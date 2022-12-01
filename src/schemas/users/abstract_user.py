from marshmallow import Schema, fields


class AbstractUser(Schema):
    email = fields.String(required=True)
    senha = fields.String(required=True)
    nome = fields.String(required=True)
    dt_nascimento = fields.String(required=True)
    cpf = fields.String(required=True)
    celular = fields.String(required=True)


class AbstractGetUser:
    pass


class BaseAdminUser(AbstractUser):
    pass
