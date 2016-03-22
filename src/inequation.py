from Polinom import Polinom
from equation import solve_equation
from enum import Enum


class Symbol(Enum):
    eq = '='
    lt = '<'
    gt = '>'
    le = '<='
    ge = '>='

def solve_inequation(polinom, symbol):
    """
    Solves inequation for polynomial p(x).
    p(x) < 0 or p(x) > 0 or ...
    Returned is a list of intervals, where x can satysfy inequation.
    >>> solve_inequation([-1,0,1], '>=')
    ['(-inf, -1]', '[1, inf)']
    """
    if not isinstance(polinom, Polinom):
        polinom = Polinom(polinom)
    if not isinstance(symbol, Symbol):
        symbol = Symbol(symbol)
    if symbol == Symbol.eq:
        return ['{' + str(i) + '}' for i in solve_equation(polinom)[1]]

    sol = [i for i in solve_equation(polinom)[1] if i.imag == 0]
    sol2 = []
    for i in set(sol):
        if sol.count(i)%2 == 1:
            sol2.append(i)
    sol = sol2
    sol.sort()
    b = polinom.coefficients[-1] < 0
    signs = [bool(i%2 == b) for i in range(len(sol)+1)]
    signs = signs[::-1]

    # make a class Interval ?
    brackets = '()' if symbol in [Symbol.gt, Symbol.lt] else '[]'
    intervals = ['(-inf, ' + str(sol[0]) + brackets[1]]
    for i in range(1, len(sol)):
        a, b = sol[i-1], sol[i]
        if a != b:
            if a == int(a): a = int(a)
            if b == int(b): b = int(b)
            a, b = str(a), str(b)
            intervals.append(brackets[0]+ a + ', ' + b + brackets[1])
    intervals.append(brackets[0] + str(sol[-1]) + ', inf)')

    out = []
    b = symbol in [Symbol.gt, Symbol.ge]
    for i in range(len(intervals)):
        if signs[i] == b:
            out.append(intervals[i])
    return out


if __name__ == '__main__':
    import doctest
    doctest.testmod()
