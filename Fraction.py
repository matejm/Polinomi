from Polinom import Polinom
import equation
from fractions import gcd as gcd_int

def gcd(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return gcd_int(a, b)
    if isinstance(a, Polinom) and isinstance(b, Polinom):
        zeros_a = set(equation.solve(a)[1])
        zeros_b = set(equation.solve(b)[1])
        zeros = list(zeros_a.intersection(zeros_b))
        p = Polinom([1])
        for i in zeros:
            p *= Polinom([-i, 1])
        return p

class Fraction:
    def __init__(self, num, denum):
        """
        >>> Fraction(1,2)
        (1) / (2)
        """
        g = gcd(num, denum)
        self.num = num // g
        self.denum = denum // g
    def __repr__(self):
        return '({}) / ({})'.format(self.num, self.denum)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
