from fastapi import FastAPI # Импорт основного класса FastAPI
from app.routers import users, task # Импорт роутеров из модулей users и task
from app.backend.db import engine, Base
import uvicorn # Импорт Uvicorn
app = FastAPI() # Создание экземпляра приложения FastAPI


@app.get("/") # Базовый маршрут
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router) # Подключение роутера task
app.include_router(users.router) # Подключение роутера users

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True) # Запуск сервера с авто-перезагрузкой при изменениях