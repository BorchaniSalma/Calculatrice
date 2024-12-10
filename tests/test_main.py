import math

import pytest
import calculatrice.main
import calculatrice.scientific
import calculatrice.statistics
from calculatrice.main import Calculator
from calculatrice.scientific import Scientific
from calculatrice.statistics import Statistics


# Test add method
def test_add():
    calc = Calculator()
    # Valid cases
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0
    assert calc.add(0.5, 1.5) == 2.0  # Testing with float numbers

# Test subtract method


def test_subtract():
    calc = Calculator()
    # Valid cases
    assert calc.subtract(10, 4) == 6
    assert calc.subtract(0, 5) == -5
    assert calc.subtract(-1, -1) == 0
    assert calc.subtract(2.5, 1.0) == 1.5  # Testing with float numbers

# Test multiply method


def test_multiply():
    calc = Calculator()
    # Valid cases
    assert calc.multiply(3, 3) == 9
    assert calc.multiply(0, 100) == 0
    assert calc.multiply(-2, 5) == -10
    assert calc.multiply(1.5, 2.0) == 3.0  # Testing with float numbers

# Test divide method


def test_divide():
    calc = Calculator()
    # Valid cases
    assert calc.divide(8, 2) == 4
    assert calc.divide(10, 2) == 5
    assert calc.divide(5, 0.5) == 10  # Testing with float numbers

    # Invalid case (division by zero)
    with pytest.raises(ValueError):
        calc.divide(10, 0)

    # Edge case for negative numbers
    assert calc.divide(-10, 2) == -5

# Test average method


def test_average():
    calc = Calculator()
    # Valid cases
    assert calc.average([1, 2, 3, 4, 5]) == 3
    assert calc.average([1.0, 2.0, 3.0]) == 2.0  # Testing with float numbers
    assert calc.average([10]) == 10  # Single number in the list

    # Invalid case (empty list)
    with pytest.raises(ValueError):
        calc.average([])

    # Edge case for empty average calculation
    assert calc.average([0, 0, 0]) == 0  # Average of zeros should be zero

    # Case for large numbers
    assert calc.average([1000000, 2000000, 3000000]) == 2000000

# Additional test for logging behavior (not common in unit tests, but useful for debugging)


def test_logging_for_operations(caplog):
    calc = Calculator()

    with caplog.at_level("INFO"):
        calc.add(2, 3)
        calc.subtract(10, 4)
        calc.multiply(3, 3)
        calc.divide(8, 2)

    assert "Adding 2 + 3" in caplog.text
    assert "Subtracting 10 - 4" in caplog.text
    assert "Multiplying 3 * 3" in caplog.text
    assert "Dividing 8 / 2" in caplog.text


def test_power():
    calc = Scientific()
    # Valid cases
    assert calc.power(2, 3) == 8  # 2^3 = 8
    assert calc.power(5, 0) == 1  # 5^0 = 1
    assert calc.power(3, -2) == 1 / 9  # 3^-2 = 1 / 9


def test_logarithm():
    calc = Scientific()
    # Valid cases
    assert math.isclose(calc.logarithm(100, 10), 2)  # log(100, 10) = 2
    assert math.isclose(calc.logarithm(8, 2), 3)  # log(8, 2) = 3
    # Default base 10
    assert math.isclose(calc.logarithm(1000), 3)  # log(1000, 10) = 3

    # Edge cases and errors
    with pytest.raises(ValueError):
        calc.logarithm(0, 10)  # Logarithm of 0 is undefined
    with pytest.raises(ValueError):
        calc.logarithm(-10, 10)  # Logarithm of negative numbers is undefined


def test_median():
    calc = Statistics()
    # Valid cases
    assert calc.median([1, 2, 3, 4, 5]) == 3
    assert calc.median([1, 3, 5]) == 3
    assert calc.median([1, 2, 3, 4]) == 2.5  # Even number of elements

    # Edge cases
    with pytest.raises(ValueError):
        calc.median([])  # Empty list


def test_standard_deviation():
    calc = Statistics()
    # Valid cases
    assert math.isclose(calc.standard_deviation(
        [1, 2, 3, 4, 5]), 1.4142135623730951, rel_tol=1e-9)
    assert math.isclose(calc.standard_deviation(
        [10, 20, 30]), 8.16496580927726, rel_tol=1e-9)

    # Edge cases
    with pytest.raises(ValueError):
        calc.standard_deviation([])  # Empty list
