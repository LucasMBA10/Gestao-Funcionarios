# models/allocation.py

from pydantic import BaseModel

class Allocation(BaseModel):
    id: int
    employee_id: int
    project_id: int
    allocated_hours: float
