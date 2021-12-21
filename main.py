
from ToDo.routers import authentication
from ToDo.routers.authentication import login
from fastapi import FastAPI
from . import models
from .database import  engine
from .routers import todo, user, authentication
app = FastAPI()
models.Base.metadata.create_all(engine)
app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(todo.router)



    






