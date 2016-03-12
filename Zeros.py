from Polinom import Polinom

def derivate(polinom):
    """
    >>> derivate(Polinom([1,2,3]))
    6x + 2
    """
    l = []
    for i in range(1, polinom.degree+1):
        l.append(polinom.coefficients[i]*i)
    return Polinom(l)

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
    pd = derivate(polinom)
    for i in range(100):
        x2 = x - polinom.value(x) / pd.value(x)
        if x == x2: return x
        x = x2
    return None

if __name__ == '__main__':
    import doctest
    doctest.testmod()
