from fastapi import FastAPI , Depends
from pydantic import BaseModel 

from app.database import engine , SessionLocal
from app.models import Base
from sqlalchemy.orm import Session

from app.models import User
from fastapi import HTTPException

import bcrypt

from app.auth import create_access_token 
from app.auth import verify_token

from typing import Optional 

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserCreate(BaseModel):
    name : str
    age : int
    email : str 
    mobile : str 
    password : str 

class UserUpdate(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    email : Optional[str] = None
    mobile : Optional[str] = None
    password : Optional[str] = None 

class UserLogin(BaseModel):
    email : str 
    password : str

#Create Users
@app.post("/register")
def register(user:UserCreate , db: Session = Depends(get_db) ):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    hashed_password = bcrypt.hashpw(
        user.password.encode("utf8"),
        bcrypt.gensalt()
    )

    new_user = User(
        name = user.name,
        age = user.age,
        email = user.email,
        mobile = user.mobile ,
        password =hashed_password.decode("utf8")
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email,
        "mobile": new_user.mobile,
        "age": new_user.age
    }

@app.post("/users/{user_id}")
def update(user_id:int ,user:UserUpdate , token_data = Depends(verify_token), db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()

    if db_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    hashed_password = bcrypt.hashpw(
        user.password.encode("utf8"),
        bcrypt.gensalt()
    )

    if user.name is not None:
        db_user.name = user.name

    if user.age is not None:
        db_user.age = user.age

    if user.email is not None:
        db_user.email = user.email

    if user.mobile is not None:
        db_user.mobile = user.mobile 

    if user.password is not None:
        db_user.password = hashed_password.decode("utf8")

    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{user_id}")
def delete(user_id:int , token_data = Depends(verify_token) , db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()

    if db_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    db.delete(db_user)
    db.commit()

    return {"message": "User deleted Successfully"}


#Read 
@app.get("/users/{user_id}")
def get_users(user_id: int , token_data = Depends(verify_token) ,db: Session = Depends(get_db)):
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user

#jwt authentication




@app.post("/login")
def login( user : UserLogin , db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if db_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    if not bcrypt.checkpw(
        user.password.encode("utf-8"),
        db_user.password.encode("utf-8")
    ) : 
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    token = create_access_token(
        {
            "user_id": db_user.id,
            "email" : db_user.email
        }
    )
    return {
        "access_token" : token ,
        "token_type" : "bearer"
    }
    
