import unittest
from calculator import Calculator, add_all

class TestCalculator(unittest.TestCase):

    # Test Calculator

    def setUp(self):
        self.calculator = Calculator()
  
    def test_add(self):
        self.assertEqual(self.calculator.add(5,5), 10)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(6,5), 1)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(5,3), 15)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6,2), 3)

    # Test divide when denominator is 0
    def test_divide_with_zero(self):
        self.assertEqual(self.calculator.divide(6,0), 'You can t divide by zero!')


class TestAddAll(unittest.TestCase):
    def test_add_all(self):
        self.assertEqual(add_all([2,2,2]), 6)

if __name__ == "__main__":
    unittest.main()