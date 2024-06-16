# employees_controller.py
from fastapi import APIRouter
from controllers.employee_controller import router as employee_router

router = APIRouter()

# Incluir os roteadores
router.include_router(employee_router)
