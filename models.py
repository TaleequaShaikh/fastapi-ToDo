import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class ToDo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String)
    done = Column(Boolean, default=False)
    due = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="todos")
    
class User(Base):  
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    todos = relationship('ToDo', back_populates="owner")


    

