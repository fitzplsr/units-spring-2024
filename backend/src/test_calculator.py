import math
import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(2, 2), 4)
        self.assertRaises(TypeError, self.calculator.addition, 1, 'string')

    def test_mul(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)

    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(2, 2), 0)
        self.assertRaises(TypeError, self.calculator.subtraction, 1, 'string')

    def test_div(self):
        self.assertEqual(self.calculator.division(8, 2), 4)
        self.assertIsNone(self.calculator.division(8, 0))
        self.assertRaises(TypeError, self.calculator.division, 1, 'string')

    def test_abs(self):
        self.assertEqual(self.calculator.adsolute(-5), 5)
        self.assertEqual(self.calculator.adsolute(5), 5)
        self.assertRaises(TypeError, self.calculator.adsolute, 'string')

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertRaises(TypeError, self.calculator.degree, 1, 'string')


    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)
        self.assertRaises(TypeError, self.calculator.ln, 'string')
        self.assertRaises(ValueError, self.calculator.ln, -1)


    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(100, 10), 2)
        self.assertRaises(ValueError, self.calculator.log, -1, 10)
        self.assertRaises(ValueError, self.calculator.log, 10, -1)
        self.assertRaises(TypeError, self.calculator.log, 1, 'string')


    def test_sqrt(self):
        self.assertAlmostEqual(self.calculator.sqrt(9), 3)
        self.assertRaises(TypeError, self.calculator.sqrt, 'string')

    def test_nth_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(8, 3), 2)
        self.assertRaises(TypeError, self.calculator.nth_root, 1, 'string')
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 1, 0)


if __name__ == "__main__":
    unittest.main()
