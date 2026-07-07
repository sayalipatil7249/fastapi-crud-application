from sqlalchemy.orm import declarative_base
from sqlalchemy import Column , Integer , String 
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True , index=True)
    name = Column(String(100) , nullable=False)
    age = Column(Integer , nullable=False)
    email = Column(String(100),unique=True , nullable=False)
    mobile = Column(String(15),unique=True , nullable = False)
    password = Column(String(255) , nullable=False)