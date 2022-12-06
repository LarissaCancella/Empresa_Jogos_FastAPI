from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy.future import select
from sqlalchemy import delete, update
import datetime

from database.models import Empresa, Jogo
from database.connection import async_session

class EmpresaService:
    async def create_empresa(nome: str, cnpj: str, endereco: str, num_func: int):
        async with async_session() as session:
            session.add(Empresa(nome=nome, cnpj=cnpj, endereco=endereco, num_func=num_func))
            await session.commit()
    
    async def update_empresa(empresa_id: int, nome: str, cnpj: str, endereco: str, num_func: int):
        async with async_session() as session:
            await session.execute(update(Empresa).where(Empresa.id==empresa_id).values(nome=nome, cnpj=cnpj, endereco=endereco, num_func=num_func))
            await session.commit()

    async def delete_empresa(empresa_id: int):
        async with async_session() as session:
            await session.execute(delete(Empresa).where(Empresa.id==empresa_id))
            await session.commit()

    async def list_empresa():
        async with async_session() as session:
            result = await session.execute(select(Empresa))
            return result.scalars().all()
    
    async def get_by_id(empresa_id):
        async with async_session() as session:
            result = await session.execute(select(Empresa).where(Empresa.id==empresa_id))
            return result.scalar()

class JogoService:
    async def add_game(empresa_id: int, nome: str, data_lancamento: datetime.datetime, num_vendas: float, plataforma: str):
        async with async_session() as session:
            session.add(Jogo(empresa_id=empresa_id, nome=nome, data_lancamento=data_lancamento, num_vendas=num_vendas, plataforma=plataforma))
            await session.commit()

    async def update_game(game_id: int, empresa_id: int, nome: str, data_lancamento: datetime.datetime, num_vendas: float, plataforma: str):
        async with async_session() as session:
            await session.execute(update(Jogo).where(Jogo.id==game_id).values(empresa_id=empresa_id, nome=nome, data_lancamento=data_lancamento, num_vendas=num_vendas, plataforma=plataforma))
            await session.commit()

    async def remove_game(game_id: int):
        async with async_session() as session:
            await session.execute(delete(Jogo).where(Jogo.id==game_id))
            await session.commit()

    async def list_games():
        async with async_session() as session:
            result = await session.execute(select(Jogo))
            return result.scalars().all()
    
    async def get_by_id(game_id):
        async with async_session() as session:
            result = await session.execute(select(Jogo).where(Jogo.id==game_id))
            return result.scalar()

    
