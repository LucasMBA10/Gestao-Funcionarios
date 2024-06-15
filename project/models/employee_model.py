from pydantic import BaseModel, Field
from datetime import datetime

class Employee(BaseModel):
    cpf: str = Field(..., pattern=r'^\d{11}$')  # CPF deve ter exatamente 11 dígitos
    name: str
    position: str
    salary: float
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
