from calculatrice.scientific import Scientific
from calculatrice.statistics import Statistics
from calculatrice.main import Calculator
import calculatrice.main
import calculatrice.scientific
import calculatrice.statistics
import pytest
import os

# current_directory = os.path.dirname(os.path.abspath(__file__))
# new_path = os.path.abspath(os.path.join(current_directory, "../"))
# os.chdir(new_path)

# comment to test


@pytest.fixture
def calc():
    return Calculator()


@pytest.fixture
def stats():
    return Statistics()


@pytest.fixture
def sci():
    return Scientific()


def test_integration_calculator_and_statistics(calc, stats):
    # Test integration between Calculator and Statistics
    numbers = [10, 20, 30, 40, 50]
    avg = calc.average(numbers)
    assert avg == 30

    median = stats.median(numbers)
    assert median == 30

    stdev = stats.standard_deviation(numbers)
    assert (
        pytest.approx(stdev, 0.01) == 14.14
    )  # Approximation for floating-point precision


def test_integration_calculator_and_scientific(calc, sci):
    # Test integration between Calculator and Scientific
    result = calc.multiply(3, 4)  # Multiply first
    power_result = sci.power(result, 2)  # Then calculate the power
    assert power_result == 144

    log_result = sci.logarithm(power_result)
    assert (
        pytest.approx(log_result, 0.01) == 2.16
    )  # Approximation for floating-point precision


def test_combined_operations(calc, stats, sci):
    # Test a complex workflow using Calculator, Statistics, and Scientific
    numbers = [2, 4, 6, 8, 10]
    avg = calc.average(numbers)  # Step 1: Average
    squared_avg = sci.power(avg, 2)  # Step 2: Square the average
    # Step 3: Calculate standard deviation
    stdev = stats.standard_deviation(numbers)
    result = calc.add(squared_avg, stdev)  # Step 4: Combine results
    assert pytest.approx(result, 0.01) == 38.83  # Updated expected value
