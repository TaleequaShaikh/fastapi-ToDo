from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database, models, oauth2
from typing import List
from sqlalchemy.orm import Session
router = APIRouter(prefix= "/todo", tags=['ToDo'])
get_db = database.get_db

@router.get('/')
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    todos = db.query(models.ToDo).all()
    return todos

@router.post('/', status_code=201)
def create_todo(request: schemas.TodoCreate, db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    new_todo = models.ToDo(task=request.task, due=request.due, user_id=1)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo 

@router.get('/{id}', status_code=200,response_model=schemas.ShowToDo)
def show(id, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    todo = db.query(models.ToDo).filter(models.ToDo.id == id).first()
    if not todo:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail':f"Task with the id {id} is not available"}
    return todo

@router.put('/{id}', status_code=201)
def update(id,response: Response,request: schemas.ToDoUpdate, db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    updated_todo = db.query(models.ToDo).filter(models.ToDo.id == id).update(request.dict())
    if not updated_todo:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail':f"Task with the id {id} is not available"}
    db.commit()
    return updated_todo


@router.delete('/todo/{id}', status_code=204)    
def destroy(id,response: Response,  db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    delete_todo = db.query(models.ToDo).filter(models.ToDo.id == id).delete(synchronize_session=False)
    if not delete_todo:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail':f"Task with the id {id} is not available"}
    db.commit()    
    return delete_todo
    
