# Makefile for Calculator Project

.PHONY: run ui dev test unit-test api-test lint format clean docker docker-up docker-down

## Run FastAPI app with Uvicorn
run:
	uvicorn main:app --reload --host 0.0.0.0 --port 8000

## Run Streamlit UI
ui:
	streamlit run streamlit_app.py

## Run FastAPI (backend) + Streamlit (frontend) together
dev:
	@echo "🚀 Starting FastAPI backend + Streamlit frontend..."
	@gnome-terminal -- bash -c "uvicorn main:app --reload --host 0.0.0.0 --port 8000; exec bash" || \
	start cmd /k "uvicorn main:app --reload --host 0.0.0.0 --port 8000" &
	@streamlit run streamlit_app.py

## Run all tests with coverage report
test:
	pytest --cov=app --cov-report=term-missing

## Run functional/unit tests only
unit-test:
	pytest func_tests

## Run API tests only
api-test:
	pytest api_test

## Lint with flake8
lint:
	flake8 app func_tests api_test main.py

## Format code with black
format:
	black app func_tests api_test main.py

## Remove __pycache__ and logs
clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
	rm -rf logs

## Build Docker image
docker:
	docker build -t calculator-api .

## Run Docker container with docker-compose
docker-up:
	docker-compose up --build

## Stop Docker container
docker-down:
	docker-compose down
