import pytest
from fraction import Fraction


# Test that a fraction is created correctly
def test_fraction_initialization():
    f = Fraction(1, 2)

    assert f.numerator == 1
    assert f.denominator == 2

# Test that the denominator cannot be 0
def test_zero_denominator():
    with pytest.raises(ValueError):
        Fraction(1, 0)

# Test that the denominator cannot be negative
def test_negative_denominator():
    with pytest.raises(ValueError):
        Fraction(1, -2)


# Test that the numerator and denominator must be integers:

# --> Test that the numerator must be an integer
def test_invalid_numerator():
    with pytest.raises(TypeError):
        Fraction(1.5, 2)


# --> Test that the denominator must be an integer
def test_invalid_denominator():
    with pytest.raises(TypeError):
        Fraction(1, 2.5)


# Test __eq__ og __ne__: 

# Test equality
def test_equal():
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 4)

    assert f1 == f2


# Test inequality
def test_not_equal():
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)

    assert f1 != f2

# Test __lt__ og __le__ 

# Test less than
def test_less_than():
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)

    assert f1 < f2


# Test less than or equal
def test_less_than_or_equal():
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 4)

    assert f1 <= f2


# Test __gt__ og __ge__: 

# Test greater than
def test_greater_than():
    f1 = Fraction(3, 4)
    f2 = Fraction(1, 2)

    assert f1 > f2


# Test greater than or equal
def test_greater_than_or_equal():
    f1 = Fraction(2, 4)
    f2 = Fraction(1, 2)

    assert f1 >= f2
