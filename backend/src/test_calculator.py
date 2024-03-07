import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_mul(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)

    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(2, 2), 0)

    def test_div(self):
        self.assertEqual(self.calculator.division(2, 2), 1)

    def test_abs(self):
        self.assertEqual(self.calculator.adsolute(-2), 2)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 2), 4)

    # def test_ln(self):
    #     self.assertEqual(self.calculator.ln(0), 1)
    #
    # def test_log(self):
    #     self.assertEqual(self.calculator.log(2, 0), 1)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(1), 1)


if __name__ == "__main__":
    unittest.main()
