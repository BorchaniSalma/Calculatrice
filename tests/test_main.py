import unittest
from calculatrice.main import Calculator


class TestCalculator(unittest.TestCase):
    """Test class for the Calculator."""

    def setUp(self):
        """Set up a Calculator instance for each test."""
        self.calc = Calculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        # Testing with float numbers
        self.assertAlmostEqual(self.calc.add(0.5, 1.5), 2.0)

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertAlmostEqual(self.calc.subtract(
            2.5, 1.0), 1.5)  # Testing with float numbers

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(3, 3), 9)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertAlmostEqual(self.calc.multiply(
            1.5, 2.0), 3.0)  # Testing with float numbers

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(10, 2), 5)
        # Testing with float numbers
        self.assertAlmostEqual(self.calc.divide(5, 0.5), 10)

        with self.assertRaises(ValueError) as cm:
            self.calc.divide(10, 0)
        self.assertEqual(str(cm.exception), "Division by zero is not allowed.")

        # Edge case for negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_average(self):
        """Test the average method."""
        self.assertEqual(self.calc.average([1, 2, 3, 4, 5]), 3)
        # Testing with float numbers
        self.assertAlmostEqual(self.calc.average([1.0, 2.0, 3.0]), 2.0)
        # Single number in the list
        self.assertEqual(self.calc.average([10]), 10)

        with self.assertRaises(ValueError) as cm:
            self.calc.average([])
        self.assertEqual(str(cm.exception),
                         "Cannot calculate the average of an empty list.")

        # Average of zeros should be zero
        self.assertEqual(self.calc.average([0, 0, 0]), 0)
        self.assertEqual(self.calc.average(
            [1000000, 2000000, 3000000]), 2000000)  # Large numbers


if __name__ == "__main__":
    unittest.main()
