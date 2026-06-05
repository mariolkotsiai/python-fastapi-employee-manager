
A REST API for managing employees built with FastAPI and SQLite. Supports full CRUD operations with automatic documentation via Swagger UI.

## Features

- Full CRUD operations (Create, Read, Update, Delete)
- SQLite database with SQLAlchemy ORM
- Data validation with Pydantic
- Auto-generated Swagger UI documentation
- Clean project structure with separated concerns

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.14+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?logo=fastapi)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightblue?logo=sqlite)

## Installation

```bash
git clone https://github.com/mariolkotsiai/python-fastapi-employee-manager.git
cd python-fastapi-employee-manager
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
uvicorn main:app --reload
```

Open your browser at `http://127.0.0.1:8000/docs` for the Swagger UI.

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /employees/ | Get all employees |
| GET | /employees/{id} | Get employee by ID |
| POST | /employees/ | Create new employee |
| PUT | /employees/{id} | Update employee |
| DELETE | /employees/{id} | Delete employee |

## Project Structure
python-fastapi-employee-manager/
├── src/
│   ├── database.py    # Database connection and session
│   ├── models.py      # SQLAlchemy models
│   ├── schemas.py     # Pydantic schemas
│   └── routes.py      # API endpoints
├── tests/             # Unit tests
├── main.py            # Application entry point
└── requirements.txt

## License

MIT License