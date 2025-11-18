# Backend (FastAPI)

## Local setup

### Fast path (recommended)

```bash
cd backend
make run        # creates venv if needed, installs deps, starts uvicorn
```

Other handy targets:

```bash
make stop       # stops uvicorn
make restart    # stop + run
make clean      # removes .venv
```

### Manual steps

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

The API exposes a health endpoint at `GET /status`.

## Project layout

```
backend/
├── main.py              # uvicorn entrypoint (imports app.create_app)
├── app/
│   ├── __init__.py      # exports create_app
│   ├── main.py          # app factory + router wiring
│   ├── core/            # config, logging, security, etc.
│   │   └── config.py
│   ├── api/
│   │   └── routes/      # APIRouter modules
│   │       └── status.py
│   ├── schemas/         # Pydantic models (empty placeholder)
│   └── services/        # Business logic (empty placeholder)
├── tests/               # pytest suite (see test_status.py)
└── Makefile             # helper commands (run/install/stop/clean)
```

Add new routers under `app/api/routes/`, schemas under `app/schemas/`, and reusable domain logic under `app/services/`.

# permis-maroc-api
