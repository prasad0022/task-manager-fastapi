from fastapi import APIRouter, HTTPException, status
from app.data import tasks
from app.schemas import Task

router = APIRouter()

def validate_task_id(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found!")
    
@router.get("/tasks")
def get_tasks(completed: bool | None = None):
    filtered_tasks = tasks
    if completed is not None:
        filtered_tasks = [
            task
            for task in tasks
            if task.completed == completed
        ]    
    return {"success": True, "count": len(filtered_tasks), "data": filtered_tasks}   

@router.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_tasks(task: Task):
    tasks.append(task)
    return {"success": True, "msg": "Task added successfully", "data": task} 

@router.get("/tasks/{task_id}")
def get_task_by_id(task_id: int):
    validate_task_id(task_id)
    return {"success": True, "data": tasks[task_id]}     

@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    validate_task_id(task_id)
    tasks[task_id] = task
    return {"success": True, "msg": "Task updated successfully", "data": tasks[task_id]} 

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    validate_task_id(task_id)
    del tasks[task_id]
    return {"success": True, "msg": "Task deleted successfully"}    