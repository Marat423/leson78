from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from app.models import *
# Определение модели Task
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer)
    completed = Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    slug = Column(String, unique=True, index=True)

    user = relationship("User", back_populates="tasks")


print(CreateTable(Task.__table__))