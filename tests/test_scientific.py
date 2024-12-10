import pytest
import math
import unittest
from calculatrice.scientific import Scientific


class TestScientificCalculator(unittest.TestCase):

    def test_power(self):
        calc = Scientific()
        # Valid cases
        self.assertEqual(calc.power(2, 3), 8)  # 2^3 = 8
        self.assertEqual(calc.power(5, 0), 1)  # 5^0 = 1
        self.assertAlmostEqual(calc.power(3, -2), 1 / 9)  # 3^-2 = 1 / 9

    def test_logarithm(self):
        calc = Scientific()
        # Valid cases
        # log(100, 10) = 2
        self.assertTrue(math.isclose(calc.logarithm(100, 10), 2))
        self.assertTrue(math.isclose(calc.logarithm(8, 2), 3))  # log(8, 2) = 3
        # Default base 10
        # log(1000, 10) = 3
        self.assertTrue(math.isclose(calc.logarithm(1000), 3))

        # Edge cases and errors
        with self.assertRaises(ValueError):
            calc.logarithm(0, 10)  # Logarithm of 0 is undefined
        with self.assertRaises(ValueError):
            # Logarithm of negative numbers is undefined
            calc.logarithm(-10, 10)


# If using pytest, the following is not necessary, but for unittest compatibility:
if __name__ == "__main__":
    unittest.main()
