from fastapi import APIRouter , Depends , status , Response , HTTPException
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from Database.database import get_db
from schemas import  schemas
from models import models
from APP import oauth2 ,utils

router = APIRouter(tags=["Authentication"])

@router.post("/login" , response_model=schemas.Token)
def login(user_credintials : OAuth2PasswordRequestForm = Depends(),db : Session = Depends(get_db)  ):
    user = db.query(models.User).filter(models.User.email == user_credintials.username).first()
    if not user :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="Invalid Credentials")
    if not utils.verify_password(user_credintials.password, user.pwd):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    access_token = oauth2.create_access_token(data={"user_id" : user.id})
    return  {"access_token" : access_token , 'token_type' : "bearer"}

@router.post("/signup")
def create_account(account  : schemas.UserCreate , db : Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == account.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    account_dict = account.model_dump()
    account_dict["pwd"] = utils.hash_password(account_dict["pwd"])
    new_user = models.User(**account_dict)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User successfully created"}
