import pandas as pd
import os
import requests
import logging
from datetime import datetime

# =========================
# CAMINHOS DO PROJETO
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CAMINHO_DADOS = os.path.join(BASE_DIR, "dados", "filmes.csv")
CAMINHO_RESULTADO = os.path.join(BASE_DIR, "resultado")
CAMINHO_LOGS = os.path.join(BASE_DIR, "logs")

CAMINHO_FILMES_PROCESSADOS = os.path.join(CAMINHO_RESULTADO, "filmes_processados.csv")
CAMINHO_RESUMO_GENERO = os.path.join(CAMINHO_RESULTADO, "resumo_por_genero.csv")
CAMINHO_LOG = os.path.join(CAMINHO_LOGS, "etl.log")

API_URL = "http://127.0.0.1:8000/filmes"

# =========================
# CONFIGURAÇÃO DE LOG
# =========================
os.makedirs(CAMINHO_LOGS, exist_ok=True)

logging.basicConfig(
    filename=CAMINHO_LOG,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# =========================
# EXTRAÇÃO
# =========================
def extrair_csv():
    logging.info("Iniciando extração do CSV")
    return pd.read_csv(CAMINHO_DADOS)

def extrair_api():
    logging.info("Iniciando extração da API")
    response = requests.get(API_URL)
    response.raise_for_status()
    return pd.DataFrame(response.json())

# =========================
# TRANSFORMAÇÃO
# =========================
def transformar(df):
    logging.info("Iniciando transformação dos dados")

    ano_atual = datetime.now().year

    df["Ano"] = pd.to_numeric(df["Ano"], errors="coerce")
    df = df.dropna(subset=["Ano"])
    df["Ano"] = df["Ano"].astype(int)

    df["Idade_filme"] = ano_atual - df["Ano"]
    df = df[df["Ano"] >= 2010]

    logging.info("Transformação concluída")
    return df

# =========================
# CARREGAMENTO
# =========================
def carregar(df):
    logging.info("Iniciando carregamento dos dados")

    os.makedirs(CAMINHO_RESULTADO, exist_ok=True)

    df.to_csv(CAMINHO_FILMES_PROCESSADOS, index=False)

    resumo = df.groupby("Genero").size().reset_index(name="Quantidade")
    resumo.to_csv(CAMINHO_RESUMO_GENERO, index=False)

    logging.info("Arquivos gerados com sucesso")

# =========================
# PIPELINE PRINCIPAL
# =========================
def main():
    try:
        logging.info("ETL iniciado")

        df_csv = extrair_csv()
        df_api = extrair_api()

        df_total = pd.concat([df_csv, df_api], ignore_index=True)
        df_final = transformar(df_total)

        carregar(df_final)

        logging.info("ETL finalizado com sucesso")
        print("ETL executado com sucesso!")

    except Exception as e:
        logging.error(f"Erro no ETL: {e}")
        print("Erro no ETL:", e)

if __name__ == "__main__":
    main()