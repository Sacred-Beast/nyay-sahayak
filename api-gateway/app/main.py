#main file for API Gateway

from fastapi import FastAPI
from .routes import router

app = FastAPI(
    title="Nyay-Sahayak API Gateway",
    description="API Gateway for Nyay-Sahayak Legal AI System",
    version="1.0.0"
)

app.include_router(router)
