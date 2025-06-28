import unittest
from app.service.core import Calculator
from app.utils.exceptions import CustomException


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add_positive(self):
        self.assertEqual(self.calc.add(3, 5), 8)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-3, -5), -8)

    def test_add_mixed(self):
        self.assertEqual(self.calc.add(10, -3), 7)

    def test_sub_positive(self):
        self.assertEqual(self.calc.sub(10, 3), 7)

    def test_sub_negative(self):
        self.assertEqual(self.calc.sub(-5, -2), -3)

    def test_sub_mixed(self):
        self.assertEqual(self.calc.sub(5, -5), 10)

    def test_mul_positive(self):
        self.assertEqual(self.calc.mul(3, 5), 15)

    def test_mul_negative(self):
        self.assertEqual(self.calc.mul(-3, -5), 15)

    def test_mul_mixed(self):
        self.assertEqual(self.calc.mul(-2, 4), -8)

    def test_mul_zero(self):
        self.assertEqual(self.calc.mul(0, 10), 0)

    def test_div_positive(self):
        self.assertEqual(self.calc.div(10, 2), 5.0)

    def test_div_negative(self):
        self.assertEqual(self.calc.div(-10, -2), 5.0)

    def test_div_mixed(self):
        self.assertEqual(self.calc.div(-10, 2), -5.0)

    def test_div_zero_numerator(self):
        self.assertEqual(self.calc.div(0, 5), 0.0)

    def test_div_zero_denominator(self):
        with self.assertRaises(CustomException):
            self.calc.div(5, 0)

    def test_div_result_precision(self):
        self.assertEqual(self.calc.div(1, 3), 0.3333)


if __name__ == '__main__':
    unittest.main()
