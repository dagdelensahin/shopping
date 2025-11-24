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
