# views/salary_history_view.py

from fastapi import APIRouter, HTTPException
from models.salary_history import SalaryHistory
from controllers.salary_history_controller import SalaryHistoryController

router = APIRouter()
salary_history_controller = SalaryHistoryController()

@router.post("/salary_histories/")
async def create_salary_history(salary_history: SalaryHistory):
    created_salary_history = salary_history_controller.create_salary_history(salary_history)
    return created_salary_history

@router.get("/salary_histories/{history_id}")
async def read_salary_history(history_id: int):
    salary_history = salary_history_controller.get_salary_history(history_id)
    if salary_history is None:
        raise HTTPException(status_code=404, detail="Salary history not found")
    return salary_history
