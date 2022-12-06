from fastapi import FastAPI, APIRouter

from views import empresa_router, jogo_router

app = FastAPI()
router = APIRouter()

app.include_router(empresa_router)
app.include_router(jogo_router)