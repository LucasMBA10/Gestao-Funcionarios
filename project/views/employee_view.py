# employees_views.py
from fastapi import APIRouter, HTTPException
from models.employee_model import Employee
import redis
import json
from datetime import datetime

router = APIRouter()

try:
    # Conexão com o Redis
    redis_client = redis.Redis(host='redis', port=6379, db=0)
    redis_client.ping()  # Verifica se é possível enviar um ping ao servidor Redis
    print("Conexão com o Redis estabelecida com sucesso!")
except redis.ConnectionError:
    print("Erro ao conectar ao Redis. Verifique as configurações ou a disponibilidade do servidor.")
    raise  # Propaga a exceção para indicar que houve um erro crítico de conexão

# Endpoint para criar um funcionário (POST)
@router.post("/employee")
async def create_employee(employee: Employee):
    try:
        employee_id = redis_client.incr('employee_id')
        employee_dict = employee.dict()
        employee_dict['created_at'] = employee_dict['created_at'].isoformat()
        employee_dict['updated_at'] = employee_dict['updated_at'].isoformat()
        redis_client.hset("employees", employee_id, json.dumps(employee_dict))
        redis_client.sadd("employee_ids", employee_id)  # Adiciona o ID do funcionário a um conjunto
        return {"id": employee_id, "employee": employee_dict}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar funcionário: {str(e)}")

# Endpoint para listar todos os funcionários criados
@router.get("/employees")
async def list_all_created_employees():
    try:
        all_employees = []

        # Recupera todos os IDs de funcionários do conjunto
        employee_ids = redis_client.smembers("employee_ids")

        for employee_id in employee_ids:
            employee_data = redis_client.hget("employees", employee_id)
            if employee_data:
                employee = json.loads(employee_data)
                employee['created_at'] = datetime.fromisoformat(employee['created_at'])
                employee['updated_at'] = datetime.fromisoformat(employee['updated_at'])
                all_employees.append({"id": int(employee_id), "employee": employee})

        return all_employees
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar funcionários: {str(e)}")
