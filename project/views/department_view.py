# views/department_view.py

from fastapi import APIRouter, HTTPException
from models.department import Department
from controllers.department_controller import DepartmentController

router = APIRouter()
department_controller = DepartmentController()

@router.post("/departments/")
async def create_department(department: Department):
    created_department = department_controller.create_department(department)
    return created_department

@router.get("/departments/{department_id}")
async def read_department(department_id: int):
    department = department_controller.get_department(department_id)
    if department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return department
