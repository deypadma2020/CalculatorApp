from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "message": "Calculator API is running"
    }


# Test Add
def test_add():
    response = client.post("/api/v1/add", json={"a": 5, "b": 7})
    assert response.status_code == 200
    assert response.json() == {"result": 12}

def test_add_negative():
    response = client.post("/api/v1/add", json={"a": -2, "b": -3})
    assert response.json()["result"] == -5

# Test Sub
def test_sub():
    response = client.post("/api/v1/sub", json={"a": 10, "b": 4})
    assert response.json()["result"] == 6

def test_sub_negative():
    response = client.post("/api/v1/sub", json={"a": -4, "b": -10})
    assert response.json()["result"] == 6

# Test Mul
def test_mul():
    response = client.post("/api/v1/mul", json={"a": 3, "b": 4})
    assert response.json()["result"] == 12

def test_mul_zero():
    response = client.post("/api/v1/mul", json={"a": 0, "b": 100})
    assert response.json()["result"] == 0

# Test Div
def test_div():
    response = client.post("/api/v1/div", json={"a": 10, "b": 2})
    assert response.json()["result"] == 5.0

def test_div_zero_numerator():
    response = client.post("/api/v1/div", json={"a": 0, "b": 5})
    assert response.json()["result"] == 0.0

def test_div_zero_denominator():
    response = client.post("/api/v1/div", json={"a": 5, "b": 0})
    assert response.status_code == 400
    assert "Division by zero" in response.json()["detail"]

# Test Precision
def test_div_precision():
    response = client.post("/api/v1/div", json={"a": 1, "b": 3})
    assert response.json()["result"] == 0.3333

# Invalid Payloads
def test_add_missing_field():
    response = client.post("/api/v1/add", json={"a": 5})
    assert response.status_code == 422

def test_invalid_type_input():
    response = client.post("/api/v1/add", json={"a": "five", "b": 5})
    assert response.status_code == 422
