from sqlalchemy.orm import Session
from models.vehicle import Vehicle
from schemas.vehicle import VehicleCreate
from fastapi import HTTPException, status


def get_car_by_plate(db: Session, plate: str):
    return db.query(Vehicle).filter(Vehicle.Plate == plate).first()

def create_vehicle(db: Session, vehicle: VehicleCreate):
    new_vehicle = Vehicle(
        plate=vehicle.plate,
        renavam=vehicle.renavam,
        brand=vehicle.brand, 
        model=vehicle.model, 
        year=vehicle.year, 
        )
    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)
    return new_vehicle


def read_vehicles(db: Session, user_id: int):
    vehicle = db.query(Vehicle).filter(Vehicle.user_id == user_id).first()

    if not vehicle:
        raise HTTPException(status_code=400, detail="Vehicle not found")

    return vehicle

def delete_vehicle(db: Session, user_id: int):
    vehicle = db.query(Vehicle).filter(Vehicle.user_id == user_id).first()
    
    if vehicle: 
        db.delete(vehicle)
        db.commit()
    else:
        raise HTTPException(status_code=400, detail="Vehicle not found")
