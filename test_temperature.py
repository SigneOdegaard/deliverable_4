#task 1 continued 

import pytest
from temperature import Temperature

#this script will test initialization, Validation, Conversion, Round-trip conversion, cross-unit comparisons and formatting of the Temperature class.

def test_default_unit():
    temp = Temperature(25)

    assert temp.unit == 'C'
    assert temp.value == 25

def test_invalid_unit():
    with pytest.raises(ValueError):
        Temperature(25, 'X')

@pytest.mark.parametrize("unit, expected", [
    ('c', 'C'),
    ('f', 'F'),
    ('k', 'K')
])
def test_case_insensitivity(unit, expected):
    temp = Temperature(25, unit)

    assert temp.unit == expected

def test_readonly_properties():
    temp = Temperature(25, 'C')

    with pytest.raises(AttributeError):
        temp.value = 30

    with pytest.raises(AttributeError):
        temp.unit = 'F'

@pytest.mark.parametrize("value, unit", [
    (-274, 'C'),
    (-460, 'F'),
    (-1, 'K')
])
def test_below_absolute_zero(value, unit):
    with pytest.raises(ValueError):
        Temperature(value, unit)


@pytest.mark.parametrize("celsius, fahrenheit, kelvin", [
    (-273.15, -459.67, 0), #Absolute zero
    (-40, -40, 233.15), #Celsius-Fahrenheit crossover
    (0, 32, 273.15), #Freezing point of water
    (37, 98.6, 310.15), #Human body temperature
    (100, 212, 373.15) #Boiling point of water
])
def test_conversion(celsius, fahrenheit, kelvin):
    temp_c = Temperature(celsius, 'C')
    temp_f = Temperature(fahrenheit, 'F')
    temp_k = Temperature(kelvin, 'K')

    assert temp_c.to_fahrenheit() == pytest.approx(
        fahrenheit, abs=1e-9, rel=0
    )
    assert temp_c.to_kelvin() == pytest.approx(
        kelvin, abs=1e-9, rel=0
    )
    assert temp_f.to_celsius() == pytest.approx(
        celsius, abs=1e-9, rel=0
    )
    assert temp_f.to_kelvin() == pytest.approx(
        kelvin, abs=1e-9, rel=0
    )
    assert temp_k.to_celsius() == pytest.approx(
        celsius, abs=1e-9, rel=0
    )
    assert temp_k.to_fahrenheit() == pytest.approx(
        fahrenheit, abs=1e-9, rel=0
    )

@pytest.mark.parametrize("value", [
    -273.15,
    -40,
    0,
    37,
    100
])
def test_round_trip_conversion(value):
    temp = Temperature(value, 'C')

    converted_temp = (
        temp.convert_to('F')
            .convert_to('K')
            .convert_to('C')
    )

    assert converted_temp == temp

@pytest.mark.parametrize("value1, unit1, value2, unit2", [
    (0, 'C', 32, 'F'),
    (0, 'C', 273.15, 'K'),
    (32, 'F', 273.15, 'K'),
    (100, 'C', 212, 'F'),
    (37, 'C', 310.15, 'K')
])
def test_cross_unit_equality(value1, unit1, value2, unit2):
    temp1 = Temperature(value1, unit1)
    temp2 = Temperature(value2, unit2)

    assert temp1 == temp2
    assert temp1 <= temp2
    assert temp1 >= temp2
    assert not temp1 != temp2

def test_cross_unit_ordering():
    cold = Temperature(0, 'C')
    hot = Temperature(300, 'K')

    assert cold != hot
    assert cold < hot
    assert cold <= hot

    assert hot > cold
    assert hot >= cold
    assert not hot < cold

@pytest.mark.parametrize("value, unit, expected_str, expected_repr", [
    (25, 'C', "25.00 °C", "Temperature(25.0, 'C')"),
    (98.6, 'F', "98.60 °F", "Temperature(98.6, 'F')"),
    (310.15, 'K', "310.15 K", "Temperature(310.15, 'K')")
])
def test_formatting(value, unit, expected_str, expected_repr):
    temp = Temperature(value, unit)

    assert str(temp) == expected_str
    assert repr(temp) == expected_repr


