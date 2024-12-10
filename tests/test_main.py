import pytest
from calculatrice.main import Calculator

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
