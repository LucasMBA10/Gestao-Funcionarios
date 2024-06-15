from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/registros", response_class=HTMLResponse)
async def get_registros(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/employee")
        funcionarios = response.json()
    return templates.TemplateResponse("registros.html", {"request": request, "funcionarios": funcionarios})
