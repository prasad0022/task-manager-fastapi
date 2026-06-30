from fastapi import FastAPI, status, HTTPException
from app.routers.tasks import router as tasks_router
from app.database import engine, Base
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tasks_router)

@app.get("/health")
def home():
    return {
        "status": "Up",
        "message": "Welcome to FastAPI"
    }