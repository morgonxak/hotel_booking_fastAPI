from sqlalchemy import JSON, Integer, String, Column
from app.database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    hashed_password = Column(String)