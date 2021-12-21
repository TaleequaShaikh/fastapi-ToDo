from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter(prefix= "/user",tags=['User'])
get_db = database.get_db




@router.post('/', status_code=201, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db : Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}', status_code=200)
def show(id:int, response: Response, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail':f"User with the id {id} is not available"}
    return user    
