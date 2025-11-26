# shopping
simple shopping web app using python and react

## Python package

This repository was converted into a Python package. Install and run locally:


```powershell
python -m venv .venv
.venv\\Scripts\\Activate.ps1
pip install -U pip
pip install -r requirements.txt
```


```powershell
shopping --help
shopping greet --name "World"
```

Run tests:

```powershell
pip install -r requirements.txt
pip install pytest
pytest
```

## Frontend (React)

A minimal React frontend scaffold using Vite is included in `frontend/`.

Quick start (PowerShell):

```powershell
cd frontend
npm install
npm run dev
```

Build for production:

```powershell
npm run build
npm run preview
```

The dev server runs on `http://localhost:5173` by default.

## Backend (Flask API)

A minimal Flask API is included at `shopping/api.py`. It has two example endpoints:

- `GET /api/hello?name=YourName` — returns a greeting JSON like `{ "message": "Hello, YourName!" }`.
- `GET /api/items` — returns a small list of sample items.

Install backend dependencies and run (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -U pip
pip install -r requirements.txt

# Run the API directly
python -m shopping.api

# Or use the console script after installing package editable/install: `shopping-api`
```

The Flask dev server listens on port `5000` by default. The frontend example fetches `http://localhost:5000/api/hello`.

## Docker Setup

Run the entire full-stack (React Frontend + Flask Backend + MySQL) using Docker Compose:

### Prerequisites
- Docker and Docker Compose installed

### Quick Start

```powershell
# Build and run all services (MySQL, Flask API, React UI)
docker-compose up --build
```

All services will start automatically:
- **Frontend** (React UI): `http://localhost:5173`
- **Backend API**: `http://localhost:5000`
- **MySQL Database**: `localhost:3306`

### Services

- **MySQL Database** — Runs on `localhost:3306`
  - Root user: `root`
  - Root password: `shopping_root_password`
  - Database: `shopping`

- **Flask Backend** — Runs on `http://localhost:5000`
  - Auto-creates database and tables on startup
  - API endpoints: `/api/hello`, `/api/items`

- **React Frontend** — Runs on `http://localhost:5173`
  - Built with Vite
  - Connects to backend API automatically

### Useful Commands

```powershell
# View logs from all services
docker-compose logs -f

# View logs from specific service
docker-compose logs -f backend
docker-compose logs -f frontend
docker-compose logs -f mysql

# Stop all services
docker-compose down

# Remove all data (including database)
docker-compose down -v

# Rebuild images (if you made code changes)
docker-compose build --no-cache

# Rebuild specific service
docker-compose build --no-cache frontend
docker-compose build --no-cache backend
```

### Accessing the Application

- **Web UI**: Open browser to `http://localhost:5173`
- **Backend API**: `http://localhost:5000/api/hello`
- **MySQL**: `mysql -h 127.0.0.1 -u root -pshopping_root_password`

### Environment Variables

Edit `docker-compose.yml` to customize:
- `MYSQL_ROOT_PASSWORD` — MySQL root password
- `DB_HOST` — Database host (default: `mysql`)
- `VITE_API_URL` — Frontend API endpoint (default: `http://backend:5000`)
