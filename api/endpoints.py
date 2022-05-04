from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from .model import jainu

jainu = jainu()
api_router = APIRouter()

templates = Jinja2Templates(directory="templates")


class text(BaseModel):
    text: str


class t_output(BaseModel):
    t_output: str


@api_router.post("/translate", response_model=t_output)
async def translate(request: text):
    return t_output(
        t_output=jainu.translate(request.text)
    )


@api_router.get("/translate/{text}", response_class=HTMLResponse)
async def translate_on_page(request: Request, text: str):
    t_output = jainu.translate(text)
    return templates.TemplateResponse("index.html", {"request": request, "text_output": t_output})


@api_router.get("/")
@api_router.get("/translate/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
