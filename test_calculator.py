# https://github.com/nickdevito22/lab10-ND-CZ
# Partner 1: Nicholas Devito
# Partner 2: Cynthia Zhang

import unittest
import math
from calculator import *

class TestCalculator(unittest.TestCase):

    # Partner 2
    def test_add(self):
        self.assertEqual(add(3, 5), 8)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 100), 2.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 100)

    # Partner 1
    def test_multiply(self):
        self.assertEqual(mul(3, 7), 21)

    def test_divide(self):
        self.assertEqual(div(2, 10), 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(-2, 100)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(16), 4.0)
        with self.assertRaises(ValueError):
            square_root(-4)

if __name__ == '__main__':
    unittest.main()
