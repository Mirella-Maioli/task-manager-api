from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task Manager API")

class Task(BaseModel):
    title: str
    description: str
    completed: bool = False

tasks = []

@app.get("/")
def home():
    return {"message": "Welcome to the Task Manager API"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {"message": "Task created", "task": task}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    if task_id < len(tasks):
        tasks[task_id] = task
        return {"message": "Task updated"}
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id < len(tasks):
        tasks.pop(task_id)
        return {"message": "Task deleted"}
    return {"error": "Task not found"}
