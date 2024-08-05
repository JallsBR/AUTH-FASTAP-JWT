from sqlalchemy import Column, String, Integer
from app.db.base import Base

class UserModel(Base):
        __table__ = "users"
        id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
        username = Column('usename', String, nullable=False, unique=True)
        password = Column ('password', String, nullable=False)