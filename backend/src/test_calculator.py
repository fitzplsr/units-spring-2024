import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_mul(self):
        self.assertEqual(self.calculator.addition(1, 2), 2)

    def test_sub(self):
        self.assertEqual(self.calculator.addition(1, 2), 2)


if __name__ == "__main__":
    unittest.main()
