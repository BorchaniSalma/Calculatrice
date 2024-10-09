import pytest

from main import Calculator


def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0


def test_subtract():
    calc = Calculator()
    assert calc.subtract(10, 4) == 6
    assert calc.subtract(0, 5) == -5


def test_multiply():
    calc = Calculator()
    assert calc.multiply(3, 3) == 9
    assert calc.multiply(0, 100) == 0


def test_divide():
    calc = Calculator()
    assert calc.divide(8, 2) == 4
    with pytest.raises(ValueError):
        calc.divide(10, 0)


def test_average():
    calc = Calculator()
    assert calc.average([1, 2, 3, 4, 5]) == 3
    with pytest.raises(ValueError):
        calc.average([])
