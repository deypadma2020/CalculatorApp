```markdown
# 🧮 Calculator API

A production-ready, modular FastAPI-based calculator project that supports both command-line interface (CLI) and REST API operations. It includes logging, custom exceptions, test automation, and Docker deployment.

---

## 📌 Project Overview

This project is a robust calculator that:

- Performs basic arithmetic operations (add, subtract, multiply, divide)
- Exposes a REST API via FastAPI
- Includes full logging and error handling
- Can be run via CLI or HTTP
- Is modular, scalable, and test-driven
- Provides health check, Docker support, and full API documentation

---

## 📁 Project Structure

```

calculator\_project/
│
├── app/                      # Application code
│   ├── api/                  # FastAPI routes
│   ├── service/              # Business logic
│   └── utils/                # Exceptions, logger
│
├── api\_test/                 # API tests using pytest
├── func\_tests/               # Unit tests using unittest
│
├── main.py                   # FastAPI app entry point
├── setup.py                  # Packaging config
├── pyproject.toml            # Modern build config
├── Makefile                  # Dev automation commands
├── Dockerfile                # Image build config
├── docker-compose.yaml       # Compose config
├── requirements.txt
└── README.md                 # You are here

````

---

## 🚀 Functionality

### ✅ API Endpoints

| Operation    | Endpoint         | Method | Example Payload          |
|--------------|------------------|--------|--------------------------|
| Add          | `/api/v1/add`    | POST   | `{ "a": 10, "b": 5 }`    |
| Subtract     | `/api/v1/sub`    | POST   | `{ "a": 10, "b": 5 }`    |
| Multiply     | `/api/v1/mul`    | POST   | `{ "a": 10, "b": 5 }`    |
| Divide       | `/api/v1/div`    | POST   | `{ "a": 10, "b": 2 }`    |
| Health Check | `/api/v1/health` | GET    | —                        |

### ✅ Sample Response

```json
{
  "result": 15
}
````

---

## 🧰 How to Use

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Run Locally

```bash
make run
```

Then open:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## ⚙️ CLI Usage (Optional)

To run calculator interactively from terminal:

```bash
python main.py
```

This mode supports step-by-step number and operator inputs via CLI.

---

## 🐳 Docker Usage

### 🔨 Build Docker Image

```bash
make docker
```

### 🚀 Run via Docker Compose

```bash
make docker-up
```

Your app will be available at: [http://localhost:8000](http://localhost:8000)

To stop:

```bash
make docker-down
```

---

## 🧪 Running Tests

### ✅ Run All Tests

```bash
make test
```

### 🧪 Run Unit (Function) Tests

```bash
make unit-test
```

### 🌐 Run API (Endpoint) Tests

```bash
make api-test
```

---

## 📬 Postman Testing Example

1. Open Postman or REST client.
2. Send a `POST` request:

```
POST http://127.0.0.1:8000/api/v1/add
Content-Type: application/json

{
  "a": 5,
  "b": 10
}
```

3. Response:

```json
{
  "result": 15
}
```

4. Try `/sub`, `/mul`, `/div`, `/health` as well.

---

## 🛠️ Developer Shortcuts via Makefile

```bash
make run          # Start API server locally
make test         # Run all tests with coverage
make unit-test    # Run function/unit tests only
make api-test     # Run API tests only
make lint         # Run flake8 linter
make format       # Format code with black
make clean        # Remove __pycache__ and logs
make docker       # Build Docker image
make docker-up    # Run with Docker Compose
make docker-down  # Stop Docker Compose
```

---

## 📄 API Docs (via Swagger & ReDoc)

After running the app:

* 📘 Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
* 📕 ReDoc UI: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🔐 Error Handling

Handled with custom exception logic for clarity.

### Example: Division by zero

```json
{
  "detail": "Error occurred in python script name [core.py] line number [10] error message[Division by zero is not allowed]"
}
```

---

## 🧱 Future Improvements

* ✅ Add exponentiation/modulus support
* 🔒 JWT authentication for API
* 🚀 Auto-deploy to AWS/Render
* 🔁 CI/CD pipeline via GitHub Actions
* 📊 Add Prometheus `/metrics` endpoint

---

## 👨‍💻 Author

**Padma Dey**
📧 [deypadma2022@gmail.com](mailto:deypadma2022@gmail.com)
🌐 [GitHub Profile](https://github.com/deypadma2020)

---

## 🪪 License

This project is licensed under the MIT License. See `LICENSE` file for details.

```

