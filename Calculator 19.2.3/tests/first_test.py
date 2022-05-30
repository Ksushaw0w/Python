import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 5, 7) == 35

    def test_multiplay_calculate_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_multiply_calculation_division(self):
        assert self.calc.division(self, 20, 10) == 2

    def test_multiply_calculation_adding(self):
        assert self.calc.adding(self, 25, 4) == 29

    def test_multiply_calculation_subtraction(self):
        assert self.calc.subtraction(self, 60, 18) == 42




