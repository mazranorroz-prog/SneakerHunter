from fastapi import FastAPI

app = FastAPI(
    title="SneakerHunter API",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "SneakerHunter API running"
    }  