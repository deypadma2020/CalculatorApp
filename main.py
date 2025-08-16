from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.calc_api import router

app = FastAPI(
    title="Calculator API",
    version="1.0.0",
    description="A simple calculator API using FastAPI"
)

# Include calculator routes
app.include_router(router, prefix="/api/v1")

# Option 1: Root welcome message
@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to Calculator API! Visit /docs for API documentation."}

# Option 2: Redirect root to Swagger docs
# Uncomment below if you prefer automatic redirect instead of message
# @app.get("/", include_in_schema=False)
# def docs_redirect():
#     return RedirectResponse(url="/docs")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
