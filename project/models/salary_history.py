# models/salary_history.py

from pydantic import BaseModel

class SalaryHistory(BaseModel):
    id: int
    employee_id: int
    change_date: str
    previous_salary: float
    new_salary: float
