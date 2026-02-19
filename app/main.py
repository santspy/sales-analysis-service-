from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Sales Analysis Service",
    description="Microserviço para análise automatizada de planilhas Excel.",
    version="1.0.0"
)

app.include_router(router)