from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from database.models import Base, RideRequest
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv

load_dotenv()

# Create tables at startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ride Request Server", version="1.0.0")

class RideRequestCreate(BaseModel):
    user_id: str
    source_location: str
    destination_location: str

class RideRequestResponse(BaseModel):
    id: int
    user_id: str
    source_location: str
    destination_location: str
    status: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

@app.post("/ride-requests", response_model=RideRequestResponse)
def create_ride_request(
    ride_request: RideRequestCreate,
    db: Session = Depends(get_database_session)
):
    """Create a new ride request and store in PostgreSQL"""
    try:
        db_ride_request = RideRequest(
            user_id=ride_request.user_id,
            source_location=ride_request.source_location,
            destination_location=ride_request.destination_location
        )

        db.add(db_ride_request)
        db.commit()
        db.refresh(db_ride_request)

        return db_ride_request.to_dict()

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.get("/ride-requests", response_model=List[RideRequestResponse])
def get_all_ride_requests(db: Session = Depends(get_database_session)):
    """Get all ride requests from PostgreSQL"""
    ride_requests = db.query(RideRequest).all()
    return [request.to_dict() for request in ride_requests]

@app.get("/ride-requests/{request_id}", response_model=RideRequestResponse)
def get_ride_request(request_id: int, db: Session = Depends(get_database_session)):
    """Get a specific ride request by ID"""
    ride_request = db.query(RideRequest).filter(RideRequest.id == request_id).first()
    if not ride_request:
        raise HTTPException(status_code=404, detail="Ride request not found")
    return ride_request.to_dict()

@app.get("/ride-requests/user/{user_id}", response_model=List[RideRequestResponse])
def get_user_ride_requests(user_id: str, db: Session = Depends(get_database_session)):
    """Get all ride requests for a specific user"""
    ride_requests = db.query(RideRequest).filter(RideRequest.user_id == user_id).all()
    return [request.to_dict() for request in ride_requests]

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "ride-request-server"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("SERVER_PORT", 8000))
    # IMPORTANT: running as a module is recommended: python -m server.main
    uvicorn.run("server.main:app", host="0.0.0.0", port=port, reload=True)
