from fastapi import FastAPI
from views import (
    allocation_view,
    department_view,
    employee_view,
    project_view,
    salary_history_view
)

app = FastAPI()

# Registrando os roteadores das views
app.include_router(allocation_view.router)
app.include_router(department_view.router)
app.include_router(employee_view.router)
app.include_router(project_view.router)
app.include_router(salary_history_view.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
