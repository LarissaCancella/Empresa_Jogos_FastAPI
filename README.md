# PROJETO COM FASTAPI

**FastAPI, PostgreSQL, Async SQLAlchemy, Docker**

## Dependecias

- Docker
- Docker-compse
- Python >= 3.10
- Pipenv

## Como rodar

Adicione o caminho do projeto a `PYTHONPATH` no arquivo `.env`.

Suba as imagens do banco de dados **postgres** e o **pgadmin** no Docker

```shell
docker-compose up -d
```

Suba o ambiente

```shell
pipenv shell
```

Instale as dependencias python

```shell
pipenv install
```

Inicialize o banco de dados

```shell
python .\database\init_db.py
```

Inicie a aplicação (na porta que preferir, ex: 8000)

```shell
uvicorn main:app --port 8000
```

## Modelo de dados

# Empresa

| id               | int   | pk  |
| ---------------- | ----- | --- |
| nome             | str   |     |
| num_funcionarios | float |     |
| endereco         | str   |     |
| cnpj             | str   |     |

# Jogo

| id              | int      | pk  |
| --------------- | -------- | --- |
| nome            | str      |     |
| num_vendas      | float    |     |
| data_lancamento | datetime |     |
| plataforma      | str      |     |
| empresa_id      | int      | fk  |
