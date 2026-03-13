from fastapi import FastAPI

app = FastAPI()

tasks = []

@app.get("/")
def home():
    return {"message": "Task Manager API"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: dict):
    tasks.append(task)
    return {"message": "Task added", "task": task}
