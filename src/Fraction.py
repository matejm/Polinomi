from Polinom import Polinom
import equation
import string_handling_fractions
from fractions import gcd as gcd_int

def gcd(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return gcd_int(a, b)
    if isinstance(a, float) or isinstance(a, int):
        a = Polinom([a])
    if isinstance(b, float) or isinstance(b, int):
        b = Polinom([b])
    if a.coefficients == [1] or b.coefficients == [1]:
        return 1
    if isinstance(a, Polinom) and isinstance(b, Polinom):
        zeros_a = set(equation.solve(a)[1])
        zeros_b = set(equation.solve(b)[1])
        zeros = list(zeros_a.intersection(zeros_b))
        p = Polinom([1])
        for i in zeros:
            p *= Polinom([-i, 1])
        return p

class Fraction:
    """
    Fraction represented with numerator and denumerator.
    Greatest common divisor of numerator and denumerator is 1
    """
    def __init__(self, num, denum):
        """
        >>> Fraction(1,2)
        (1) / (2)
        """
        if denum == 0 or denum == Polinom([0]):
            raise ZeroDivisionError("Fraction denumerator cannot be 0.")
        g = gcd(num, denum)
        self.num = num // g
        self.denum = denum // g

    def __add__(self, other):
        """
        >>> Fraction(3, 10) + Fraction(7, 4)
        (41) / (20)
        >>> Fraction(1, 3) + 1
        (4) / (3)
        """
        if isinstance(other, float) or isinstance(other, int) or isinstance(other, Polinom):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            num = self.num * other.denum + self.denum * other.num
            denum = self.denum * other.denum
            return Fraction(num, denum)
        raise TypeError('Invalid operation for Polinom and '+type(other).__name__)

    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        """
        >>> -Fraction(-3, 4)
        (3) / (4)
        """
        return Fraction(-self.num, self.denum)

    def __mul__(self, other):
        """
        >>> Fraction(5, 4) * Fraction(2, 3)
        (5) / (6)
        """
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, Polinom):
            return Fraction(other * self.num, self.denum)
        if isinstance(other, Fraction):
            return Fraction(self.num * other.num, self.denum * other.denum)
        raise TypeError('Invalid operation for Fraction and '+type(other).__name__)

    def __truediv__(self, other):
        """
        >>> Fraction(5, 4) / Fraction(2, 3)
        (15) / (8)
        """
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, Polinom):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return self * other.inverse()
        raise TypeError('Invalid operation for Fraction and '+type(other).__name__)

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.num == other.num and self.denum == other.denum
        return False

    def inverse(self):
        """
        >>> Fraction(1, 3).inverse()
        (3) / (1)
        """
        return Fraction(self.denum, self.num)

    def __repr__(self):
        return string_handling_fractions.fraction_to_string(self)

    def __getitem__(self, x):
        """
        >>> Fraction(Polinom('x-1'), Polinom('x'))[2]
        0.5
        """
        num, denum = self.num, self.denum
        if isinstance(self.num, Polinom): num = self.num[x]
        if isinstance(self.denum, Polinom): denum = self.denum[x]
        return num / denum

    value = __getitem__


if __name__ == '__main__':
    import doctest
    doctest.testmod()
