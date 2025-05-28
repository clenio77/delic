from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database.database import Base, engine
from backend.api.routers import licitacoes # Importe outros routers aqui

# Criar as tabelas no DB
Base.metadata.create_all(bind=engine)

app = FastAPI(title="DELIC Agents API")

# Configurar CORS para permitir requisições do frontend Vue.js
origins = [
    "http://localhost:5173", # Porta padrão do Vite/Vue dev server
    # Adicione aqui o URL de produção do seu frontend quando for para produção
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(licitacoes.router, prefix="/api") # Prefixo para todas as rotas da API

@app.get("/")
async def root():
    return {"message": "Bem-vindo à API dos Agentes DELIC!"}