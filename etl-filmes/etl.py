import pandas as pd
import os

# Caminhos
entrada = "dados_filmes.csv"
saida = "resultado/filmes_processados.csv"

# EXTRAÇÃO
df = pd.read_csv(entrada)

# TRANSFORMAÇÃO
df["Ano"] = df["Ano"].astype(int)
df["Idade_filme"] = 2025 - df["Ano"]

df_filtrado = df[df["Ano"] >= 2010]

# CARREGAMENTO
os.makedirs("resultado", exist_ok=True)
df_filtrado.to_csv(saida, index=False)

print("ETL finalizado! Arquivo gerado em:", saida)
