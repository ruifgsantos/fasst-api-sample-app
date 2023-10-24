from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("template.html", {"request": request})


@app.get("/{name}", response_class=HTMLResponse)
async def home_page(request: Request, name: str):
    return templates.TemplateResponse("template2.html", {"request": request, "name": name})


@app.get("/home")
async def message():
    return {"message": "Hello World"}
