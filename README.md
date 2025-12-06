# Projeto ETL de Filmes
Este projeto realiza um processo completo de ETL (Extract, Transform, Load) utilizando Python e a biblioteca pandas, processando dados de filmes a partir de um arquivo CSV.

---

## Estrutura do Projeto
etl-filmes/
├── dados_filmes.csv
├── etl.py
├── resultado/
│   └── filmes_processados.csv
└── README.md

---

## Objetivo
O projeto tem como objetivo:
- Ler dados brutos sobre filmes
- Transformar esses dados
- Gerar um arquivo final limpo e padronizado

---

## Etapas do ETL

### EXTRACT — Extração
O script lê o arquivo dados_filmes.csv, contendo:
Titulo,Ano,Genero
A Origem,2010,Ficção
Interestelar,2014,Ficção
Divertida Mente,2015,Animação

### TRANSFORM — Transformação
Transformações realizadas:
- Cálculo da idade do filme
- Padronização dos tipos
- Organização dos dados

Exemplo do resultado transformado:
Titulo,Ano,Genero,Idade_filme
A Origem,2010,Ficção,15
Interestelar,2014,Ficção,11
Divertida Mente,2015,Animação,10

### LOAD — Carregamento
O arquivo final é salvo em:
resultado/filmes_processados.csv

---

## Como executar o projeto
1. Instale o pandas:
pip install pandas

2. Navegue até a pasta etl-filmes

3. Execute:
python etl.py

---

## Tecnologias utilizadas
- Python 3
- Pandas
- CSV

---

## Autor
Projeto desenvolvido por **Rhayanne Matos** como parte do Desafio ETL — Bootcamp Santander 2025 - Ciência de Dados com Python (DIO).
