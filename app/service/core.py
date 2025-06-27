from app.utils.exceptions import CustomException
import sys

class Calculator:
    def add(self, a: float, b: float) -> float: return a + b
    def sub(self, a: float, b: float) -> float: return a - b
    def mul(self, a: float, b: float) -> float: return a * b

    def div(self, a: float, b: float) -> float:
        try:
            return round(a / b, 4)
        except ZeroDivisionError as e:
            raise CustomException("Division by zero is not allowed", sys)
