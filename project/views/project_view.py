# views/project_view.py

from fastapi import APIRouter, HTTPException
from models.project import Project
from controllers.project_controller import ProjectController

router = APIRouter()
project_controller = ProjectController()

@router.post("/projects/")
async def create_project(project: Project):
    created_project = project_controller.create_project(project)
    return created_project

@router.get("/projects/{project_id}")
async def read_project(project_id: int):
    project = project_controller.get_project(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project
