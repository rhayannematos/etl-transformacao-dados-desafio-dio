# Projeto ETL de Filmes com API

Este projeto implementa um pipeline completo de **ETL (Extract, Transform, Load)** em Python, integrando **dados de um arquivo CSV** com **dados provenientes de uma API REST**, realizando tratamento, transformação e geração de arquivos finais prontos para análise.

---

## Estrutura do Projeto

```
📂 etl-filmes/
├── api/
│   ├── api_filmes.py          # API simulada com FastAPI
│   └── dados_api.json         # Base de dados da API
│
├── etl/
│   └── etl.py                 # Pipeline ETL principal
│
├── dados/
│   └── filmes.csv             # Dados brutos em CSV
│
├── resultado/
│   ├── filmes_processados.csv # Resultado final do ETL
│   └── resumo_por_genero.csv  # Agregação por gênero
│
├── logs/
│   └── etl.log                # Log de execução do ETL
│
├── requirements.txt
└── README.md
```

---

## Objetivo do Projeto

O projeto tem como objetivo demonstrar, de forma prática:

* Integração de múltiplas fontes de dados (CSV + API)
* Tratamento de dados inconsistentes
* Aplicação de regras de negócio
* Geração de arquivos analíticos
* Uso de boas práticas como logging e organização de projeto

---

## Etapas do ETL

### EXTRACT — Extração

Os dados são extraídos a partir de duas fontes:

1. **Arquivo CSV** localizado em `dados/filmes.csv`
2. **API REST** criada com FastAPI, acessada via endpoint:

```
http://127.0.0.1:8000/filmes
```

---

### TRANSFORM — Transformação

As transformações realizadas incluem:

* Conversão segura do campo `Ano` para numérico
* Remoção de registros com dados inválidos
* Cálculo da idade do filme (`Idade_filme`)
* Filtro de filmes lançados a partir de 2010
* Consolidação dos dados do CSV e da API

**Exemplo de saída transformada:**

```
Titulo,Ano,Genero,Idade_filme
A Origem,2010,Ficção,15
Interestelar,2014,Ficção,11
Divertida Mente,2015,Animação,10
```

---

### LOAD — Carregamento

Os dados processados são salvos automaticamente em:

* `resultado/filmes_processados.csv`
* `resultado/resumo_por_genero.csv`

Além disso, todo o processo é registrado em:

* `logs/etl.log`

---

## Como Executar o Projeto

### 1. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 2. Subir a API

Na raiz do projeto, execute:

```bash
uvicorn api.api_filmes:app --reload
```

A API ficará disponível em:

```
http://127.0.0.1:8000/docs
```

---

### 3. Executar o ETL

Em outro terminal, ainda na raiz do projeto:

```bash
python etl/etl.py
```

---

## Tecnologias Utilizadas

* Python 3
* Pandas
* FastAPI
* Uvicorn
* Requests
* CSV / JSON

---

## Diferenciais do Projeto

* Integração com API REST
* Tratamento de dados ausentes
* Logging estruturado
* Organização profissional de pastas
* Projeto pronto para portfólio

---

## Autor

Projeto desenvolvido por **Rhayanne Matos** como parte do Desafio ETL — Bootcamp Santander 2025 — Ciência de Dados com Python (DIO).
