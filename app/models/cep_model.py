from datetime import datetime

from sqlalchemy import Column, Integer, String

from app.configs.database import db, ma


class CepModel(db.Model):
    __tablename__ = "cep"
    id = Column(Integer, primary_key=True)
    cep = Column(String(100), nullable=False, unique=True)
    logradouro = Column(String(100))
    complemento = Column(String(100))
    localidade = Column(String(100))
    bairro = Column(String(100))
    uf = Column(String(2))
    ibge = Column(String(100))
    gia = Column(String)
    ddd = Column(String(2))
    siafi = Column(String(100))
    validated = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DATETIME, default=datetime.now().replace(microsecond=0))


class CepSchema(ma.SQLAlchemySchema):
    class Meta:
        model = CepModel
        ordered = True
        fields = ('id', 'cep', 'logradouro', 'complemento', 'localidade', 'bairro', 'uf', 'ibge', 'gia', 'ddd', 'siafi',
                  'validated', 'created_at')