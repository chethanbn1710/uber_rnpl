Getting Started

Follow these steps to run the Uber RNPL Ride Request System locally:

Clone the repository

git clone https://github.com/chethanbn1710/uber_rnpl.git
cd uber_rnpl


Set up a virtual environment

python -m venv venv        # Create a virtual environment
venv\Scripts\activate      # Activate it on Windows
# (On Mac/Linux: source venv/bin/activate)


Install dependencies

pip install --upgrade pip
pip install -r requirements.txt


⚠️ If psycopg2-binary fails, version 2.9.10 works on Windows and is included in the requirements.

Configure environment variables

Create a .env file in the project root based on .env.example:

DATABASE_URL=sqlite:///./test.db
SERVER_HOST=0.0.0.0
SERVER_PORT=8000
CLIENT_PORT=8001


Start the server

uvicorn server.main:app --reload


The server runs at: http://127.0.0.1:8000

Swagger API docs available at: http://127.0.0.1:8000/docs

Test the API

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


Stop the server

Press CTRL + C in the terminal.

✅ Now the system is ready to accept ride requests and store them in the database.
