from sqlalchemy import Column, Integer, String, ForeignKey,Text
from db import Base

class User(Base):
    __table__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100) , unique = True)
    password = Column(String(100))