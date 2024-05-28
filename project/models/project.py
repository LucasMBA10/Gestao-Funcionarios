# models/project.py

from pydantic import BaseModel

class Project(BaseModel):
    id: int
    name: str
    description: str
    start_date: str
    end_date: str
    department_id: int
