from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from views.employee_view import router as employee_view_router
from controllers.employee_controller import router as employee_controller_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens, mas você pode especificar as origens permitidas
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

app.include_router(employee_view_router)
app.include_router(employee_controller_router)
