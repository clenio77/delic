from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import os
import json

app = FastAPI()

# Monta o diretório 'frontend/build' para ser servido na raiz ('/')
# O nome do diretório dentro do contêiner é /app/frontend/build
app.mount("/", StaticFiles(directory="/app/frontend/build", html=True), name="static")

@app.get("/api")
def read_root():
    """
    Endpoint de teste para verificar se a API está online.
    Retorna uma mensagem simples.
    """
    return {"Hello": "World"}

@app.get("/api/licitacoes")
def get_licitacoes():
    """
    Retorna a lista de licitações processadas, lidas do arquivo JSON.
    Se o arquivo não existir, retorna lista vazia.
    """
    file_path = os.path.join(os.path.dirname(__file__), '../data/processed_licitacoes.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return JSONResponse(content=data)
    except FileNotFoundError:
        return JSONResponse(content=[], status_code=200)
    except json.JSONDecodeError:
        return JSONResponse(content={"error": "Erro ao ler o arquivo de licitações."}, status_code=500)

# Adicione aqui outros endpoints da sua API
