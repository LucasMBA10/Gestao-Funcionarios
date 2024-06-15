from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import  employee_controller
from views import employee_view

app = FastAPI()

# Permitir CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employee_view.router)
app.include_router(employee_controller.router)
