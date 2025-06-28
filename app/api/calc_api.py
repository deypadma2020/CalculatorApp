from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.service.core import Calculator
from app.utils.exceptions import CustomException

router = APIRouter()
calc = Calculator()


class CalcRequest(BaseModel):
    a: float
    b: float


@router.get("/health", tags=["Health Check"])
def health_check():
    return {"status": "ok", "message": "Calculator API is running"}


@router.post("/add")
def add(req: CalcRequest):
    return {"result": calc.add(req.a, req.b)}


@router.post("/sub")
def sub(req: CalcRequest):
    return {"result": calc.sub(req.a, req.b)}


@router.post("/mul")
def mul(req: CalcRequest):
    return {"result": calc.mul(req.a, req.b)}


@router.post("/div")
def div(req: CalcRequest):
    try:
        return {"result": calc.div(req.a, req.b)}
    except CustomException as ce:
        raise HTTPException(status_code=400, detail=str(ce))
