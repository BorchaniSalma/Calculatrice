import math
from typing import List

class Statistics:
    """A module for advanced statistical operations."""

    def median(self, numbers: List[float]) -> float:
        """Calculates the median of a list of numbers."""
        if not numbers:
            raise ValueError("Cannot calculate the median of an empty list.")
        sorted_numbers = sorted(numbers)
        mid = len(sorted_numbers) // 2
        if len(sorted_numbers) % 2 == 0:
            return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
        return sorted_numbers[mid]

    def standard_deviation(self, numbers: List[float]) -> float:
        """Calculates the standard deviation of a list of numbers."""
        if not numbers:
            raise ValueError("Cannot calculate standard deviation of an empty list.")
        mean = sum(numbers) / len(numbers)
        variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
        return math.sqrt(variance)
