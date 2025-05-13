from sqlalchemy.orm import Session
from models.vehicle import Vehicle
from schemas.vehicle import VehicleCreate


def get_car_by_plate(db: Session, plate: str):
    return db.query(Vehicle).filter(Vehicle.Plate == plate).first()

def create_vehicle(db: Session, vehicle: VehicleCreate):
    new_vehicle = Vehicle(plate=vehicle.plate, model=vehicle.model, year=vehicle.year)