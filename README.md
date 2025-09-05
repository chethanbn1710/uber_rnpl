🚀 Getting Started: Ride Now Pay Later (RNPL) System

This guide walks through setting up the Ride Request System (Client + Server) locally using Python and SQLite for testing.

1️⃣ Clone the Repository
git clone https://github.com/chethanbn1710/uber_rnpl.git
cd uber_rnpl

2️⃣ Create and Activate Virtual Environment
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
# source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt


⚠️ Note: On Windows, psycopg2-binary (PostgreSQL driver) can fail to install. For quick testing, the system uses SQLite by default.

4️⃣ Configure Environment Variables

Copy .env.example to .env:

copy .env.example .env


Modify .env:

DATABASE_URL=sqlite:///./test.db   # Use SQLite for testing
SERVER_HOST=0.0.0.0
SERVER_PORT=8000
CLIENT_PORT=8001


This ensures the system runs without PostgreSQL setup.

5️⃣ Run the Server
uvicorn server.main:app --reload


Server runs at: http://127.0.0.1:8000

Swagger docs: http://127.0.0.1:8000/docs

6️⃣ Run the Client API (Optional)

In a new terminal (same virtual environment):

uvicorn client.api:app --reload


Client API runs at: http://127.0.0.1:8001

Submit requests via Client API instead of Server directly.

7️⃣ Test Ride Requests

Using curl (Server):

curl -X POST "http://127.0.0.1:8000/ride-requests" \
-H "Content-Type: application/json" \
-d '{
  "user_id": "user123",
  "source_location": "Downtown Mall",
  "destination_location": "Airport Terminal 1"
}'


Using curl (Client):

curl -X POST "http://127.0.0.1:8001/submit-ride-request" \
-H "Content-Type: application/json" \
-d '{
  "user_id": "user123",
  "source_location": "Downtown Mall",
  "destination_location": "Airport Terminal 1"
}'


View all requests (Server):

curl -X GET "http://127.0.0.1:8000/ride-requests"


View user-specific requests (Client):

curl -X GET "http://127.0.0.1:8001/ride-requests/user123"

8️⃣ Verify Database (SQLite)

The SQLite database file test.db is created in the project root.

You can inspect it with tools like DB Browser for SQLite or sqlite3 CLI:

sqlite3 test.db
sqlite> .tables
sqlite> SELECT * FROM ride_requests;

9️⃣ Notes

This setup uses SQLite for ease of testing. For production or PostgreSQL, update DATABASE_URL in .env and install psycopg2-binary.

Make sure your virtual environment is activated every time before running the server or client.
