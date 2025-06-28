from fastapi import FastAPI
from app.api.calc_api import router

app = FastAPI(
    title="Calculator API",
    version="1.0.0",
    description="A simple calculator API using FastAPI"
)

app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
