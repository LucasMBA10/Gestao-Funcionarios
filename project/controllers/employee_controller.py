from fastapi import APIRouter
from models.employee_model import Employee

router = APIRouter()
funcionarios = []

@router.post("/employee")
async def create_employee(employee: Employee):
    funcionarios.append(employee)
    return {"message": "Employee created"}

@router.get("/employee")
async def get_employees():
    return funcionarios
