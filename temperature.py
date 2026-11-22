# task 1

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

    def convert_to(self, target_unit: str) -> Temperature:
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

