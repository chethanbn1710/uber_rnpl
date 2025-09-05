# uber_rnpl — Ride Request System with PostgreSQL

Prototype ride-hailing system (Ride Now Pay Later idea-friendly) with a **Client API** and **Server**.
- Client API accepts `user_id`, `source_location`, `destination_location` and forwards to Server.
- Server stores into PostgreSQL via SQLAlchemy.
- Test via Postman or curl.

## Quickstart

### 0) Prereqs
- Python 3.10+
- Git
- PostgreSQL **or** Docker (compose) for local DB
- (Optional) Postman

### 1) Clone & Setup
```bash
git clone https://github.com/<your-username>/uber_rnpl.git
cd uber_rnpl
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# macOS/Linux
# source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
```

### 2) Start PostgreSQL
Using Docker (recommended):
```bash
docker compose up -d
```
or install Postgres locally and create:
```sql
CREATE DATABASE ride_requests_db;
CREATE USER ride_user WITH PASSWORD 'ride_password';
GRANT ALL PRIVILEGES ON DATABASE ride_requests_db TO ride_user;
```

### 3) Run the Server and Client (from repo root)
```bash
# Server
python -m server.main
# Client (in a new terminal)
python -m client.api
```

### 4) Curl Tests
Submit via Client API (port 8001):
```bash
curl -X POST "http://localhost:8001/submit-ride-request"   -H "Content-Type: application/json"   -d '{"user_id":"user123","source_location":"Downtown Mall","destination_location":"Airport T1"}'
```

Get user requests via Client:
```bash
curl -X GET "http://localhost:8001/ride-requests/user123"
```

Directly hit Server (port 8000):
```bash
curl -X POST "http://localhost:8000/ride-requests"   -H "Content-Type: application/json"   -d '{"user_id":"user456","source_location":"Central Station","destination_location":"Business District"}'
```

### 5) Verify in Postgres
```sql
SELECT * FROM ride_requests;
SELECT * FROM ride_requests WHERE user_id='user123';
```

### 6) Add collaborator
- Repo → Settings → Collaborators → **Add people** → `vinayrao123` → Write access.

## Notes
- Run using `python -m server.main` and `python -m client.api` so that package imports work.
- Env vars live in `.env`. Adjust ports or DB URL as needed.
