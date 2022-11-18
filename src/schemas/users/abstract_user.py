from marshmallow import Schema, fields


class AbstractUser(Schema):
    email = fields.String()
    senha = fields.String()
    nome = fields.String()
    dt_nascimento = fields.String()
    cpf = fields.String()
    celular = fields.String()


class AbstractGetUser

class BaseAdminUser(AbstractUser):
    pass



