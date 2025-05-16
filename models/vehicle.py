from sqlalchemy import Column, String, Integer, Date, ForeignKey, BigInteger
from db.session import Base

class Vehicle(Base):
    __tablename__: 'Vehicles'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    plate = Column(String, nullable=False)
    renavam = Column(BigInteger, nullable=False)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Date, nullable=False)