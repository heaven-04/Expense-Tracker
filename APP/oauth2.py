from fastapi import HTTPException , status
from fastapi.params import Depends
from jose import JWTError , jwt
import datetime
from schemas import schemas
from fastapi.security import  OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY ="5a7740280d186936742895453d8289bf708166954f54120d542330a984cc45a9"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data : dict):
    to_encode = data.copy()
    expire  = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp" : expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)


def verify_access_token(token  : str , credentials_exception) :
    try :
        payload  = jwt.decode(token , SECRET_KEY , algorithms=ALGORITHM)
        id = payload.get("user_id")
        if not id :
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWTError :
        raise credentials_exception
    return token_data

def get_current_user(token  : str = Depends(oauth2_scheme)) :
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED ,
                                          detail=f"could not validate credentials",
                                          headers={"WWW-Authenticate" : "Bearer"})
    return verify_access_token(token , credentials_exception)
