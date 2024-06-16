from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from project.controllers.employee_controller import router as employee_router

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitações de qualquer origem
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP (GET, POST, PUT, etc.)
    allow_headers=["*"],  # Permitir todos os cabeçalhos HTTP
)

# Incluir os roteadores
app.include_router(employee_router)

@app.get("/")
async def read_root():
    return {"message": "Hello World"}
