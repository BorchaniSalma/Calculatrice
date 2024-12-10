# tests/test_simple.py
from calculatrice.main import Calculator


def test_simple():
    calc = Calculator()
    assert calc.add(1, 1) == 2
