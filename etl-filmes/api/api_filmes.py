from fastapi import FastAPI
import json
import os

app = FastAPI(
    title="API de Filmes",
    description="API simulada para o desafio de ETL da DIO",
    version="1.0.0"
)

# Caminho absoluto até a pasta onde este arquivo está
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Caminho correto do JSON
JSON_PATH = os.path.join(BASE_DIR, "dados_api.json")

# Carrega os dados do JSON
with open(JSON_PATH, encoding="utf-8") as f:
    filmes = json.load(f)


@app.get("/")
def home():
    return {"mensagem": "API de Filmes está rodando com sucesso 🚀"}


@app.get("/filmes")
def listar_filmes():
    return filmes


@app.get("/filmes/{genero}")
def filmes_por_genero(genero: str):
    return [
        filme for filme in filmes
        if filme["genero"].lower() == genero.lower()
    ]
