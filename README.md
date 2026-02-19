# Sales Analysis Service

Microserviço REST para análise automatizada de planilhas Excel.

## Arquitetura

- API Layer (FastAPI)
- Service Layer
- Domain Layer
- Infrastructure Layer
- Testes unitários
- Docker

## Executar localmente

uvicorn app.main:app --reload

Acesse: http://localhost:8000/docs

## Docker

docker build -t sales-analysis-service .
docker run -p 8000:8000 sales-analysis-service

## Endpoint

POST /analisar

Parâmetros:
- file (Excel)
- coluna (nome da coluna de vendas)