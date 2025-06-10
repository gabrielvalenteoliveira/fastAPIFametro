from sqlalchemy import Column, String, Integer, ForeignKey, BigInteger
from db.session import Base

class Vehicle(Base):
    __tablename__ = 'Vehicle'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    plate = Column(String, nullable=False)
    renavam = Column(BigInteger, nullable=False)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    vehicle_year = Column(Integer, nullable=False)