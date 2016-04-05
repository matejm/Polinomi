import Fraction
import Polinom
import re

def fraction_to_string(fraction):
    """
    >>> fraction_to_string(Fraction.Fraction(3, 7))
    '(3) / (7)'
    """
    return '({}) / ({})'.format(fraction.num, fraction.denum)

def string_to_fraction(string):
    """
    >>> string_to_fraction('(x + 1) / (x - 1)')
    (x + 1) / (x - 1)
    """
    if all((i in string for i in '()/')):
        l = re.findall('\((.*?)\)', string)
        if len(l) == 2:
            return Fraction.Fraction(Polinom.Polinom(l[0]), Polinom.Polinom(l[1]))
        elif len(l) == 1:
            return Fraction.Fraction(Polinom.Polinom(l[0]), 1)
    return Fraction.Fraction(0, 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
