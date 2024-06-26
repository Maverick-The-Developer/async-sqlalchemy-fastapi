import uvicorn
from fastapi import FastAPI, HTTPException, Depends, status
from typing import List
from schema import TodoCreate, TodoUpdate, TodoInDB
from database import asyncSessionLocal as session
import service

app = FastAPI()

@app.post("/todo" , response_model=TodoInDB, status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoCreate):
    result = await service.create_todo(session, todo.description, todo.completed)
    if result is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to create todo")
    return result

@app.get("/todo", response_model=List[TodoInDB])
async def listup_todos():
    return await service.get_all_todos(session)

@app.patch("/todo/{id}", response_model=TodoInDB)
async def update_todo(id: int, todo: TodoUpdate):
    result = await service.update_todo(session, id, todo.description, todo.completed)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return result

@app.delete("/todo/{id}")
async def delete_todo(id: int):
    result = await service.delete_todo(session, id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return result
