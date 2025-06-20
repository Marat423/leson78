from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from app.models import *
# Определение модели User
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship("Task", back_populates="user")



print(CreateTable(User.__table__))