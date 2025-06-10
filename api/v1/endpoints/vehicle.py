from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from db.session import SessionLocal
from schemas.vehicle import VehicleCreate
from services.vehicle import created_vehicle, read_vehicles, delete_vehicle


vehicle_router = APIRouter(prefix="/vehicles", tags=["vehicles"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()


@vehicle_router.post('/create', status_code=status.HTTP_201_CREATED)
def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    vehicle_created = created_vehicle(db, vehicle)
    return vehicle_created

@vehicle_router.get('/get_all_vehicles/{user_id}', status_code=status.HTTP_202_ACCEPTED)
def get_vehicles(user_id: int, db: Session = Depends(get_db)):
    read_vehicle = read_vehicles(db, user_id)
    return read_vehicles

@vehicle_router.delete('/delete_vehicle/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
def remove_vehicle(user_id: int, db: Session = Depends(get_db)):
    deleted_vehicles = delete_vehicle(db, user_id)
    return deleted_vehicles