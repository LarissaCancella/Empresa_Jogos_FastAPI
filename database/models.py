from sqlalchemy import Column, DateTime, Float, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Empresa(Base):
    __tablename__ = 'empresa'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    cnpj = Column(String)
    num_func = Column(Integer)
    endereco = Column(String)
    jogos = relationship('Jogo', backref='empresa', lazy='subquery')


class Jogo(Base):
    __tablename__ = 'jogo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    data_lancamento = Column(DateTime(timezone=True))
    num_vendas = Column(Float)
    plataforma = Column(String)
    empresa_id = Column(Integer, ForeignKey('empresa.id'))