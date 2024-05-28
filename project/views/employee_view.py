# views/employee_view.py

from fastapi import APIRouter, HTTPException
from models.employee import Employee
from controllers.employee_controller import EmployeeController

router = APIRouter()
employee_controller = EmployeeController()

@router.post("/employees/")
async def create_employee(employee: Employee):
    created_employee = employee_controller.create_employee(employee)
    return created_employee

@router.get("/employees/{employee_id}")
async def read_employee(employee_id: int):
    employee = employee_controller.get_employee(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee
