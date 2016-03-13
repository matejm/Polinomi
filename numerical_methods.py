from Polinom import Polinom
from methods import derivative


def Bisection(a, b, polinom):
    """
    Returns real zero of a polinom p(x) in interval [a,b],
    f(a) and f(b) should have opposite signs.
    >>> Bisection(1, 0, [-1, 1, 1])
    0.6180339887498949
    """
    if not isinstance(polinom, Polinom):
        polinom = Polinom(polinom)

    v = polinom.value(a)
    last_v = polinom.value(b)
    if (v < 0) == (last_v < 0): return None
    if polinom.value(a) < 0:
        a, b = b, a

    while v != last_v:
        c = (a+b)/2
        last_v = v
        v = polinom.value(c)
        if v > 0: a = c
        else: b = c
    return c

def Tangent(x, polinom):
    """
    Returns real zero of a polinom p(x).
    >>> Tangent(0, [-1, 1, 1])
    0.6180339887498948
    """
    if not isinstance(polinom, Polinom):
        polinom = Polinom(polinom)
    pd = derivative(polinom)
    for i in range(100):
        x2 = x - polinom.value(x) / pd.value(x)
        if x == x2: return x
        x = x2
    return None

def Iteration(x, polinom):
    """
    Not always correct !!
    Returns real zero of a polinom p(x).
    >>> Iteration(0.5, [-1, 1, 1])
    0.6180339887498946
    """
    if isinstance(polinom, Polinom):
        polinom = polinom.coefficients
    degree = len(polinom)
    *list, An = polinom
    polinom = -Polinom(list)
    p = lambda x: pow(polinom.value(x)/An, 1/(degree-1))
    for i in range(5000):
        x = p(x)
    return x


if __name__ == '__main__':
    import doctest
    doctest.testmod()
