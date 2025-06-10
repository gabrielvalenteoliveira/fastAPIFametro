import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from api.v1.endpoints.user import user_router
from api.v1.endpoints.vehicle import vehicle_router
from api.v1.endpoints.company import company_router
from api.v1.endpoints.auth import auth_router
from fastapi import FastAPI
from db.session import Base, engine


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(vehicle_router)
app.include_router(auth_router)
app.include_router(company_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)