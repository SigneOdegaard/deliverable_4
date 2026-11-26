
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator               # Stores the counter in the object.
        self.denominator = denominator           # Stores the denominator in the object.
        
        # Check the numerator (= integer)
        if not isinstance(numerator, int):
            raise TypeError("Numerator must be an integer")

        # Check the denominator (= integer)
        if not isinstance(denominator, int):
            raise TypeError("Denominator must be an integer")
        
        # Check the denominator (= not zero)
        if denominator <= 0:
            raise ValueError("Denominator must be positive")


        self.numerator = numerator
        self.denominator = denominator
        

    
        
    # Comparison operators

        # Check if two fractions are equal
    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        
        return self.numerator * other.denominator == other.numerator * self.denominator

    # Checks whether two fractions are not equal.
    def __ne__(self, other):
        if not isinstance(other, Fraction):
            
            return NotImplemented
        
        return not self.__eq__(other)

    # --> It uses __eq__ from the method above, but reverses the result using not

    # Checks whether one fraction is smaller than another
    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        
        return self.numerator * other.denominator < other.numerator * self.denominator


    # Checks wether the fraction is less than or equal to another
    def __le__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        
        return self.numerator * other.denominator <= other.numerator * self.denominator


    # Checks whether one fraction is greater than another
    def __gt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        
        return self.numerator * other.denominator > other.numerator * self.denominator

    # Checks whether one fraction is greater than or equal to another
    def __ge__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        
        return self.numerator * other.denominator >= other.numerator * self.denominator 

    

# Other special methods

# addition-method: 
    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        new_numerator = (
            self.numerator * other.denominator
            + other.numerator * self.denominator
        )

        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)


# subtraction-method:
    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        new_numerator = (
            self.numerator * other.denominator
            - other.numerator * self.denominator
        )

        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)

# Multiplication-method:
    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)


# Method - String representation of the fraction
# --> determines how a fraction should be displayed as text when we use print() or str() in Python
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

