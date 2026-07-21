from fastapi import FastAPI

from app.database.connection import engine

app = FastAPI(
    title="SneakerHunter API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "SneakerHunter API is running",
        "database": engine.url.render_as_string(hide_password=True)
    }