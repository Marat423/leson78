from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from sqlalchemy import Column, Integer, String
# Создание подключения к базе данных SQLite
engine = create_engine("sqlite:///taskmanager.db", echo=True)
# Создание сессий
SessionLocal = sessionmaker(bind=engine)
# Базовый класс
class Base(DeclarativeBase):
    pass
