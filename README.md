Follow these steps to run the Uber RNPL Ride Request System locally:

# 1. Clone the repository:

git clone https://github.com/chethanbn1710/uber_rnpl.git
cd uber_rnpl


# 2. Set up a virtual environment:

python -m venv venv  

venv\Scripts\activate       

# 3. Install dependencies:

pip install --upgrade pip
pip install -r requirements.txt


# 4. Configure environment variables:

Create a .env file in the project root based on .env.example:

DATABASE_URL=sqlite:///./test.db
SERVER_HOST=0.0.0.0
SERVER_PORT=8000
CLIENT_PORT=8001


# 5. Start the server:

uvicorn server.main:app --reload


Server runs at: http://127.0.0.1:8000

Swagger API docs: http://127.0.0.1:8000/docs

Test the API:

POST /ride-requests – Create a new ride request:

{
  "user_id": "user123",
  "source_location": "Downtown Mall",
  "destination_location": "Airport Terminal 1"
}


Using curl:

curl -X POST "http://127.0.0.1:8000/ride-requests" \
-H "Content-Type: application/json" \
-d '{"user_id":"user123","source_location":"Downtown Mall","destination_location":"Airport Terminal 1"}'


GET /ride-requests – Retrieve all ride requests:

curl -X GET "http://127.0.0.1:8000/ride-requests"


# 7.Stop the server:

Press CTRL + C in the terminal.

The system is now ready to accept ride requests and store them in the database.
