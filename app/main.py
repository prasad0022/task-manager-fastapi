from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def home():
    return {
        "status": "Up",
        "message": "Welcome to FastAPI"
        }