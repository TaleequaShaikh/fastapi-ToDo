from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional




class Todo(BaseModel):
    task: str
    done: bool = False
    due: datetime
    class Config():
        orm_mode = True  
    

class TodoCreate(Todo):
    pass


class ToDoUpdate(BaseModel):
    task: str
    done: bool = False

class Todo(Todo):
    id: int
    done: bool = False



class User(BaseModel):
    name: str
    email: str
    password: str
class ShowUser(BaseModel):
    name: str
    email: str
    todos: List[Todo] = []
    class Config():
        orm_mode = True  

class ShowToDo(BaseModel):
    task: str
    done: bool = False
    due: datetime
    owner: ShowUser
    class Config():
        orm_mode = True    

class Login(BaseModel):
    username: str
    password: str                

class TokenData(BaseModel):
    access_token: str
    token_type: str
class TokenData(BaseModel):
    email: Optional[str] = None       
