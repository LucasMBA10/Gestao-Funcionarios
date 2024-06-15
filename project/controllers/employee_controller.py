from fastapi import APIRouter, HTTPException
from models.employee_model import Employee
from typing import List
from datetime import datetime

router = APIRouter()

# Simulating a database
db: List[Employee] = []

@router.post("/employee", response_model=Employee)
async def create_employee(employee: Employee):
    # Check if an employee with the same CPF already exists
    if any(emp.cpf == employee.cpf for emp in db):
        raise HTTPException(status_code=400, detail="Employee with this CPF already exists")
    
    employee.created_at = datetime.now()
    employee.updated_at = datetime.now()
    db.append(employee)
    return employee

@router.get("/employee", response_model=List[Employee])
async def get_employees():
    return db
