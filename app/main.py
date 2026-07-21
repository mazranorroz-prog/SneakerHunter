from fastapi import FastAPI

from app.database.connection import Base, engine

# Import models so SQLAlchemy registers them
from app.models import Sneaker

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SneakerHunter API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "SneakerHunter API is running"
    }