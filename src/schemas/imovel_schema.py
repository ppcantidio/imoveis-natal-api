from marshmallow import Schema, fields


class Imovel(Schema):
    endereco = fields.Str()
    preco = fields.Str()
    qtd_quartos = fields.Int()
    qtd_suites = fields.Int()
    qtd_quartos = fields.Int()
    qtd_vagas_garagem = fields.Int()
    


class Apartamento(Imovel):
    andar = fields.Integer()

class Casa(Imovel):
    pass
