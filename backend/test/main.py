from typing import Union
from fastapi import FastAPI, Request
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dataType import loginData
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


templates = Jinja2Templates(directory="templates")

class t(BaseModel):
    line : str

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    context = {}
    context["request"] = request
    return templates.TemplateResponse("login.html", context)

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

