import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# test


class Calculator:
    """A simple calculator class to perform basic operations."""

    def add(self, a: float, b: float) -> float:
        """Returns the sum of two numbers."""
        result = a + b
        logger.info(f"Adding {a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        """Returns the difference between two numbers."""
        result = a - b
        logger.info(f"Subtracting {a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        """Returns the product of two numbers."""
        result = a * b
        logger.info(f"Multiplying {a} * {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        """Returns the division of two numbers. Raises an error if dividing by zero."""
        if b == 0:
            logger.error("Division by zero is not allowed.")
            raise ValueError("Division by zero is not allowed.")
        result = a / b
        logger.info(f"Dividing {a} / {b} = {result}")
        return result

    def average(self, numbers: List[float]) -> float:
        """Returns the average of a list of numbers."""
        if not numbers:
            logger.warning("The list is empty. Cannot calculate the average.")
            raise ValueError("Cannot calculate the average of an empty list.")
        result = sum(numbers) / len(numbers)
        logger.info(f"Calculating the average of {numbers} = {result}")
        return result
