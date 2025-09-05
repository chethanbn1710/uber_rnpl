from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Ride Request Client API", version="1.0.0")

SERVER_URL = f"http://localhost:{os.getenv('SERVER_PORT', 8000)}"

class RideRequestInput(BaseModel):
    user_id: str
    source_location: str
    destination_location: str

@app.post("/submit-ride-request")
def submit_ride_request(ride_request: RideRequestInput):
    """Client API endpoint to submit ride request to server"""
    try:
        # Forward request to server
        response = requests.post(
            f"{SERVER_URL}/ride-requests",
            json={
                "user_id": ride_request.user_id,
                "source_location": ride_request.source_location,
                "destination_location": ride_request.destination_location
            },
            timeout=30
        )

        if response.status_code in (200, 201):
            return {
                "status": "success",
                "message": "Ride request submitted successfully",
                "data": response.json()
            }
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Server error: {response.text}"
            )

    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=503,
            detail=f"Could not connect to server: {str(e)}"
        )

@app.get("/ride-requests/{user_id}")
def get_user_requests(user_id: str):
    """Get all ride requests for a user"""
    try:
        response = requests.get(f"{SERVER_URL}/ride-requests/user/{user_id}", timeout=30)
        if response.status_code == 200:
            return {
                "status": "success",
                "data": response.json()
            }
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=503, detail=f"Server connection error: {str(e)}")

@app.get("/health")
def health_check():
    """Client API health check"""
    return {"status": "healthy", "service": "ride-request-client-api"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("CLIENT_PORT", 8001))
    # IMPORTANT: running as a module is recommended: python -m client.api
    uvicorn.run("client.api:app", host="0.0.0.0", port=port, reload=True)
