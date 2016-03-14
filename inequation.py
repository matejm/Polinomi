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
    sol.sort()
    signs = [bool(i%2) for i in range(len(sol)+1)]
    if polinom.coefficients[-1] > 0:
        signs.pop(0)
        signs.append(not(signs[-1]))

    # make a class Interval ?
    brackets = '()' if symbol in [Symbol.gt, Symbol.lt] else '[]'
    intervals = ['(-inf, ' + str(sol[0]) + brackets[1]]
    for i in range(1, len(sol)):
        intervals.append(brackets[0]+ str(sol[i-1]) + ',' + str(sol[i]) + brackets[1])
    intervals.append(brackets[0] + str(sol[-1]) + ', inf)')

    out = []
    b = symbol in [Symbol.gt, Symbol.ge]
    for i in range(len(signs)):
        if signs[i] == b:
            out.append(intervals[i])
    return out


if __name__ == '__main__':
    import doctest
    doctest.testmod()
