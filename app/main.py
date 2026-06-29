from fastapi import FastAPI, status, HTTPException
from app.routers.tasks import router as tasks_router

app = FastAPI()

app.include_router(tasks_router)

@app.get("/health")
def home():
    return {
        "status": "Up",
        "message": "Welcome to FastAPI"
    }