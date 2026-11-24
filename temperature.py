# task 1

import math

class Temperature:
    """
    Represents a temperature in Celsius, Fahrenheit or Kelvin.

    Supports conversion between temperature units, cross-unit comparisons
    and numerical comparisons using a tolelarance of 1e-9.
    
    Args:
        value (float): The temperature value.
        unit (str): The unit of the temperature ('C', 'F', or 'K'). Defaults to 'C'.
    
    Raises: 
        ValueError: if the unit is invalid or the temperatue is below absolute zero.

    """
    TOLERANCE = 1e-9

    def __init__(self, value: float, unit: str = 'C'):
        self._value = float(value)
        self._unit = unit.upper()

        if self._unit not in ['C', 'F', 'K']:
            raise ValueError("Invalid unit. Use 'C', 'F' or 'K'.")
        
        if self._unit == 'C' and self._value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")

        if self._unit == 'F' and self._value < -459.67:
            raise ValueError("Temperature cannot be below absolute zero")

        if self._unit == 'K' and self._value < 0:
            raise ValueError("Temperature cannot be below absolute zero")

    @property
    def value(self) -> float:
        """Return the temperature value."""
        return self._value

    @property
    def unit(self) -> str:
        """Return the temperature unit."""
        return self._unit

    def to_celsius(self) -> float:
        """Return the temperature converted to celsius."""
        if self._unit == 'C':
            return self._value
        if self._unit == 'F':
            return (self._value - 32) * 5/9
        if self._unit == 'K':
            return self._value - 273.15

    def to_fahrenheit(self) -> float:
        """Return the temperature converted to fahrenheit."""
        if self._unit == 'F':
            return self._value
        elif self._unit == 'C':
            return (self._value * 9/5) + 32
        elif self._unit == 'K':
            return (self._value - 273.15) * 9/5 + 32

    def to_kelvin(self) -> float:
        """Return the temperature converted to kelvin."""
        if self._unit == 'K':
            return self._value
        elif self._unit == 'C':
            return self._value + 273.15
        elif self._unit == 'F':
            return (self._value - 32) * 5/9 + 273.15

    def convert_to(self, target_unit: str) -> "Temperature":
        """
        Returns a new Temperature instance in the specified unit.

        Args:
            target_unit (str): The unit to convert to ('C', 'F', or 'K').
        
        Returns:
            Temperature: A new Temperature instance in the specified unit.
        
        Raises:
            ValueError: If the target unit is invalid.
        """
        target_unit = target_unit.upper()

        if target_unit == 'C':
            return Temperature(self.to_celsius(), 'C')
        
        elif target_unit == 'F':
            return Temperature(self.to_fahrenheit(), 'F')
        
        elif target_unit == 'K':
            return Temperature(self.to_kelvin(), 'K')
        
        else:
            raise ValueError("Invalid target unit. Use 'C', 'F', or 'K'.")

    def __repr__(self) -> str:
        """Return an unambiguous representation of theTemperature instance."""
        return f"Temperature: {self._value}, '{self._unit}')"

    def __str__(self) -> str:
        """Returns a human-readable string formatted to two decimal places."""
        if self._unit == 'K':
            return f"{self._value:.2f} K"

        return f"{self._value:.2f} °{self._unit}"

    def __eq__(self, other):
        """Check if two Temperature instances are equal within the tolerance of 1e-9."""
        if not isinstance(other, Temperature):
            return NotImplemented
        
        return math.isclose(
            self.to_celsius(),
            other.to_celsius(),
            rel_tol=0,
            abs_tol=self.TOLERANCE
            )

    def __ne__(self, other):
        """Check if two Temperature instances are not equal within the tolerance of 1e-9."""
        if not isinstance(other, Temperature):
            return NotImplemented
        
        return not self.__eq__(other)

    def __lt__(self, other):
        """Check if this Temperature instance is less than another within the tolerance of 1e-9."""
        if not isinstance(other, Temperature):
            return NotImplemented
        
        return self.to_celsius() < other.to_celsius() and self != other

    def __le__(self, other):
        """Check if this Temperature instance is less than or equal to another within the tolerance of 1e-9."""
        if not isinstance(other, Temperature):
            return NotImplemented
        
        return self < other or self == other

    def __gt__(self, other):
        """Check if this Temperature instance is greater than another within the tolerance of 1e-9."""
        if not isinstance(other, Temperature):
            return NotImplemented
        
        return self.to_celsius() > other.to_celsius() and self != other

    def __ge__(self, other):
        """Check if this Temperature instance is greater than or equal to another within the tolerance of 1e-9."""
        if not isinstance(other, Temperature):
            return NotImplemented
        
        return self > other or self == other



a = Temperature(0, 'C')
b = Temperature(32, 'F')
c = Temperature(300, 'K')

print(a == b)
print(a != b)
print(a < c)
print(a <= b)
print(c < a)
print(c >= b)

