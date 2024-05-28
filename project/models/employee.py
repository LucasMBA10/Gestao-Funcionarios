# models/employee.py

from pydantic import BaseModel
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str
    surname: str
    date_of_birth: str
    date_of_hire: str
    position: str
    salary: float
    department_id: int
    supervisor_id: Optional[int] = None
