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

