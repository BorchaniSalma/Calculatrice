import pytest
import math
import calculatrice.main
import calculatrice.scientific
import calculatrice.statistics
from calculatrice.statistics import Statistics


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
