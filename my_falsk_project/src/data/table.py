from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()

class user(Base):
    __tablename__ = 'TB_USERS'

    userId = Column(String(255), primary_key=True)
    userPassword = Column(String(255))
    userName = Column(String(255))
