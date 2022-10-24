
import token
from jose import JWTError, jwt
from datetime import datetime, timedelta
# from . import schemas, database, models
from .import database,models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app import schemas
from .config import settings
#secret key
#algoritham
#expire time

oauth2_schema=OAuth2PasswordBearer(tokenUrl='login')

# SECRET_KEY='5d2309e5bb73b864f989753887fe52f79ce5270395e25862da6940d5'
# ALGORITHM ='HS256'
# ACCESS_TOKEN_EXPIRE_MINUTES=30
SECRET_KEY=settings.secret_key
ALGORITHM =settings.algoritham
ACCESS_TOKEN_EXPIRE_MINUTES=settings.access_token_expire_minutes


def create_access_token(data : dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp":expire})
    # to_encode.update({"exp": expire})

    encode_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encode_jwt   

def verify_access_token(access_token:str,cred_exception):
      try:

        payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        id:str=payload.get('user_id')

        if id is None:
            raise cred_exception

        token_data=schemas.TokenData(id=id) 
      except JWTError:
        raise cred_exception

      return token_data   

def get_current_user(token:str=Depends(oauth2_schema),db:Session = Depends(database.get_db)):

 credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

 token_db=verify_access_token(token,credentials_exception)
 user=db.query(models.User).filter(models.User.id==token_db.id).first()
 return user   
