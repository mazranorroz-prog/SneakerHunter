from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from config import PROJECT_NAME, TARGETS


app = FastAPI(
    title=PROJECT_NAME
)


templates = Jinja2Templates(
    directory="templates"
)


app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


@app.get("/")
def dashboard(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "targets": TARGETS
        }
    )


@app.get("/api/status")
def status():

    return {
        "status": "online",
        "target": TARGETS[0]["name"]
    }
