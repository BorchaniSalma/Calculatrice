import math

class Scientific:
    """A module for advanced scientific calculations."""

    def power(self, base: float, exponent: float) -> float:
        """Calculates the power of a number."""
        return base ** exponent

    def logarithm(self, value: float, base: float = 10) -> float:
        """Calculates the logarithm of a number to a given base."""
        if value <= 0:
            raise ValueError("Logarithm undefined for non-positive values.")
        return math.log(value, base)
