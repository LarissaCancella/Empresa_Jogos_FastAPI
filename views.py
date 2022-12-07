from typing import List

from fastapi import APIRouter, HTTPException
from starlette import responses

from schemas import (
    StandardOutput, 
    EmpresaCreateInput, 
    ErrorOutput,
    EmpresaJogosAddInput, 
    EmpresaListOutput, 
    JogoListOutput
)

from services import EmpresaService, JogoService

empresa_router = APIRouter(prefix='/empresa')
jogo_router = APIRouter(prefix='/jogos')

@empresa_router.post('/create', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def empresa_create(empresa_input: EmpresaCreateInput):
    try:
        await EmpresaService.create_empresa(nome=empresa_input.nome, cnpj=empresa_input.cnpj, endereco=empresa_input.endereco, num_func=empresa_input.num_func)
        return StandardOutput(message='Empresa cadastrada com sucesso!') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@empresa_router.delete('/delete/{empresa_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def empresa_delete(empresa_id: int):
    try:
        await EmpresaService.delete_empresa(empresa_id)
        return StandardOutput(message='Empresa removida com sucesso!') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@empresa_router.put('/update/{empresa_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def empresa_update(empresa_id: int, empresa_input: EmpresaCreateInput):
    try:
        await EmpresaService.update_empresa(empresa_id=empresa_id, nome=empresa_input.nome, cnpj=empresa_input.cnpj, endereco=empresa_input.endereco, num_func=empresa_input.num_func)
        return StandardOutput(message='Empresa atualizada com sucesso!') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@empresa_router.get('/list', response_model=List[EmpresaListOutput], responses={400: {'model': ErrorOutput}})
async def empresa_list():
    try:
        return await EmpresaService.list_empresa()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@empresa_router.get('/list/{empresa_id}', response_model=EmpresaListOutput, responses={400: {'model': ErrorOutput}})
async def empresa_list_by_id(empresa_id: int):
    try:
        return await EmpresaService.get_by_id(empresa_id=empresa_id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@jogo_router.post('/add', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def jogo_add(jogo_add: EmpresaJogosAddInput):
    try:
        await JogoService.add_jogo(empresa_id=jogo_add.empresa_id, nome=jogo_add.nome, data_lancamento=jogo_add.data_lancamento, num_vendas=jogo_add.num_vendas, plataforma=jogo_add.plataforma)
        return StandardOutput(message='Jogo cadastrado com sucesso!') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@jogo_router.delete('/remove/{jogo_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def jogo_remove(jogo_id: int):
    try:
        await JogoService.remove_jogo(jogo_id=jogo_id) 
        return StandardOutput(message='Jogo removido com sucesso!') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@jogo_router.put('/update/{jogo_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def jogo_update(jogo_id: int, jogo_input: EmpresaJogosAddInput):
    try:
        await JogoService.update_jogo(jogo_id=jogo_id, empresa_id=jogo_input.empresa_id, nome=jogo_input.nome, data_lancamento=jogo_input.data_lancamento, num_vendas=jogo_input.num_vendas, plataforma=jogo_input.plataforma)
        return StandardOutput(message='Jogo atualizado com sucesso!') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@jogo_router.get('/list', response_model=List[JogoListOutput], responses={400: {'model': ErrorOutput}})
async def jogos_list():
    try:
        return await JogoService.list_jogos()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@jogo_router.get('/list/{jogo_id}', response_model=JogoListOutput, responses={400: {'model': ErrorOutput}})
async def jogos_list_by_id(jogo_id: int):
    try:
        return await JogoService.get_by_id(jogo_id=jogo_id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))



