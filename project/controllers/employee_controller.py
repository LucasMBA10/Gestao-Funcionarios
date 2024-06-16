from fastapi import APIRouter, HTTPException
from models.employee_model import Employee
import redis
import json
from datetime import datetime

router = APIRouter()

# Conexão com o Redis
redis_client = redis.Redis(host='redis', port=6379, db=0)

# Endpoint para criar um funcionário (POST)
@router.post("/employee")
async def create_employee(employee: Employee):
    employee_id = redis_client.incr('employee_id')
    employee_dict = employee.dict()
    employee_dict['created_at'] = employee_dict['created_at'].isoformat()
    employee_dict['updated_at'] = employee_dict['updated_at'].isoformat()
    redis_client.hset("employees", employee_id, json.dumps(employee_dict))
    return {"id": employee_id, "employee": employee_dict}

# Endpoint para listar todos os funcionários (GET)
@router.get("/employees")
async def list_employees():
    employees = []
    for key in redis_client.hkeys("employees"):
        employee = json.loads(redis_client.hget("employees", key))
        employee['created_at'] = datetime.fromisoformat(employee['created_at'])
        employee['updated_at'] = datetime.fromisoformat(employee['updated_at'])
        employees.append({"id": int(key), "employee": employee})
    return employees
