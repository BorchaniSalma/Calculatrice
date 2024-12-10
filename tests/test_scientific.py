import pytest
import math
import calculatrice.main
import calculatrice.scientific
import calculatrice.statistics
from calculatrice.scientific import Scientific


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
