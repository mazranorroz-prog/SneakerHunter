from fastapi import FastAPI
from config import PROJECT_NAME


app = FastAPI(
    title=PROJECT_NAME
)


@app.get("/")
def home():

    return {
        "status": "online",
        "message": "Sneaker Hunter is running"
    }


@app.get("/targets")
def targets():

    from config import TARGETS

    return TARGETS
