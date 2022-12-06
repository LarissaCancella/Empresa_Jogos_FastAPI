from pydantic import BaseModel
from typing import List
import datetime

class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True

class EmpresaCreateInput(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    num_func: int

class EmpresaJogosAddInput(BaseModel):
    empresa_id: int
    nome: str
    data_lancamento: datetime.datetime
    num_vendas: float
    plataforma: str

class StandardOutput(BaseModel):
    message: str

class ErrorOutput(BaseModel):
    detail: str

class Jogo(OurBaseModel):
    id: int
    nome: str
    data_lancamento: datetime.datetime
    num_vendas: float
    plataforma: str
    empresa_id: int

    class Config:
        orm_mode = True

class EmpresaListOutput(OurBaseModel):
    id: int
    nome: str
    cnpj: str
    endereco: str
    num_func: int
    jogos: List[Jogo]

    class Config:
        orm_mode = True

class JogoListOutput(OurBaseModel):
    id: int
    nome: str
    data_lancamento: datetime.datetime
    num_vendas: float
    plataforma: str
    empresa_id: int

    class Config:
        orm_mode = True

