from sqlalchemy import Column, Integer, String, Date
from db.session import Base

class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=true, index=true)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    cpf = Column(String, nullable=False, unique=True)
    phone = Column(String, unique=True)
    birthdate = Column(Date, nullable=False)