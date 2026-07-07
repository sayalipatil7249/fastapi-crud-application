from jose import jwt
from dotenv import load_dotenv
import os   
from fastapi import HTTPException
from jose import JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import  Depends

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data:dict):
    token = jwt.encode(   # it returns jwt token 
        data,
        SECRET_KEY ,
        algorithm= ALGORITHM
    )
    return token 

def verify_token(token:str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token ,
            SECRET_KEY ,
            algorithms = [ALGORITHM]
        )
        return payload
    except JWTError:
        raise HTTPException(
            status_code= 401,
            detail="Invalid Token "
        )