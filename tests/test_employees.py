import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from src.database import get_db, Base

SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to Employee Manager API"


def test_create_employee():
    response = client.post("/employees/", json={
        "name": "Test User",
        "email": "testuser@company.com",
        "department": "Engineering",
        "position": "Developer",
        "salary": 50000,
        "is_active": True
    })
    assert response.status_code == 201
    assert response.json()["name"] == "Test User"


def test_get_all_employees():
    response = client.get("/employees/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_employee_by_id():
    create = client.post("/employees/", json={
        "name": "Test User",
        "email": "testuser@company.com",
        "department": "Engineering",
        "position": "Developer",
        "salary": 50000,
        "is_active": True
    })
    employee_id = create.json()["id"]
    response = client.get(f"/employees/{employee_id}")
    assert response.status_code == 200
    assert response.json()["id"] == employee_id


def test_get_employee_not_found():
    response = client.get("/employees/999")
    assert response.status_code == 404


def test_update_employee():
    create = client.post("/employees/", json={
        "name": "Test User",
        "email": "testuser@company.com",
        "department": "Engineering",
        "position": "Developer",
        "salary": 50000,
        "is_active": True
    })
    employee_id = create.json()["id"]
    response = client.put(f"/employees/{employee_id}", json={"salary": 60000})
    assert response.status_code == 200
    assert response.json()["salary"] == 60000


def test_delete_employee():
    create = client.post("/employees/", json={
        "name": "Test User",
        "email": "testuser@company.com",
        "department": "Engineering",
        "position": "Developer",
        "salary": 50000,
        "is_active": True
    })
    employee_id = create.json()["id"]
    response = client.delete(f"/employees/{employee_id}")
    assert response.status_code == 204