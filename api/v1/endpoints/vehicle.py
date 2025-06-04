from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from db.session import SessionLocal
from schemas.vehicle import VehicleCreate
from services.vehicle import create_vehicle, read_vehicles, delete_vehicle


vehicle_router = APIRouter(prefix="/vehicles", tags=["vehicles"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()


@vehicle_route.post('/create', status_code=status.HTTP_201_CREATED)
async def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    return create_vehicle(db, vehicle)

@vehicle_route.get('/get_all_vehicles', status_code=status.HTTP_202_ACCEPTED)
async def get_vehicles(user_id: int, db: Session = Depends(get_db)):
    return read_vehicles(db, user_id)

@vehicle_route.delete('/delete_vehicle', status_code=status.HTTP_204_NO_CONTENT)
async def remove_vehicle(user_id: int, db: Session = Depends(get_db)):
    return delete_vehicle(db, user_id)