from fastapi import APIRouter, HTTPException, Depends, status
from app.database import get_db
from sqlalchemy.orm import Session
from app import crud, schemas

router = APIRouter()
    
@router.get("/tasks", response_model=list[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db), completed: bool | None = None):
    filtered_tasks = crud.get_tasks(db)
    if completed is not None:
        filtered_tasks = [
            task
            for task in filtered_tasks
            if task.completed == completed
        ]
    return filtered_tasks      

@router.post("/tasks", response_model=schemas.TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@router.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(404, "Task not found")
    return task    

@router.patch("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    updated_task = crud.update_task(db, task_id, task)
    if not updated_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return updated_task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted_task = crud.delete_task(db, task_id)
    if not deleted_task:
        raise HTTPException(404, "Task not found")
    return {"message": "Task deleted successfully"} 