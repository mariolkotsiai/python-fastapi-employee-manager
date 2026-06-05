from fastapi import FastAPI
from src.database import engine
from src import models
from src.routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Manager API",
    description="A REST API for managing employees built with FastAPI and SQLite",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Welcome to Employee Manager API", "docs": "/docs"}