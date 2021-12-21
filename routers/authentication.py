from ToDo import schemas
from fastapi import APIRouter, Depends,  status, Response 
from .. import schemas, database, models, token
from sqlalchemy.orm import Session
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter(tags = ['Authentication'])
get_db = database.get_db
@router.post('/login')
def login( response: Response,request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail':f"Invalid Credentials"}
    if not Hash.verify(user.password, request.password): 
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail':f"Incorrect Password"}   
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
