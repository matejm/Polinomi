from Polinom import Polinom
from methods import horners_method, get_divisors
import cmath


def solve_linear(polinom):
    """
    >>> solve_linear([3,5])
    -0.6
    """
    b, a = polinom
    return -b/a

def solve_quadratic(polinom):
    """
    >>> solve_quadratic([-3, 2, 1])
    (-3, 1)
    """
    c, b, a = polinom
    D = b**2 - 4*a*c
    x1 = (-b - cmath.sqrt(D)) / (2*a)
    x2 = (-b + cmath.sqrt(D)) / (2*a)
    if x1 == x1.real:
        x1 = x1.real
        x2 = x2.real
    if x1 == int(x1): x1 = int(x1)
    if x2 == int(x2): x2 = int(x2)
    return x1, x2

def solve_cubic(polinom):
    """
    >>> solve_cubic([0,1,2,1])
    (-1, 0, -1)
    """
    d, c, b, a = polinom
    u = 1, complex(-0.5, cmath.sqrt(3)/2), complex(-0.5, -cmath.sqrt(3)/2)
    D = 18*a*b*c*d - 4*b**3*d + b**2*c**2 - 4*a*c**3 - 27*a**2*d**2
    D0 = b**2 - 3*a*c
    D1 = 2*b**3 - 9*a*b*c + 27*a**2*d
    C = pow((D1 + cmath.sqrt(-27*a**2 * D))/2, 1/3)
    x = []
    for i in range(3):
        xi = -1/(3*a) * (b + C*u[i] + D0/(u[i]*C))
        xi = complex(round(xi.real, 10), round(xi.imag, 10))
        if not xi.imag:
            xi = xi.real
            if xi == int(xi): xi = int(xi)
        x.append(xi)
    return tuple(x)

def solve_equation(polinom):
    """
    Solves the equation for polinom p(x)
    p(x) = 0
    Returns 0 if no solutions.
    Returns -1 if every real number is a solution.
    Returns -2 if I don't know (yet) how to solve equation.
    (e.g equation has 4 or more irrational or complex zeros)
    >>> solve([0])
    (-1, ())
    """
    if isinstance(polinom, Polinom):
        polinom = polinom.coefficients
    l = len(polinom)
    if l == 0:
        polinom.append(0)
    if l == 1:
        if polinom[0] == 0:
            return -1, tuple()
        else:
            return 0, tuple()
    elif l == 2:
        return 1, (solve_linear(polinom))
    elif l == 3:
        return 2, solve_quadratic(polinom)
    elif l == 4:
        return 3, solve_cubic(polinom)
    elif all([i == int(i) for i in polinom]):
        c = get_divisors(polinom[0]) + [0]
        d = get_divisors(polinom[1])
        candidats = set()
        for num in c:
            for denum in d:
                candidats.add(num/denum)
        for can in candidats:
            polinom2, remainder = horners_method(polinom, can)
            if not remainder:
                number, solutions = solve(polinom2)
                if number != -2: number += 1
                return number, tuple(list(solutions)+[can])
    return -2, ()

solve = solve_equation

if __name__ == '__main__':
    import doctest
    doctest.testmod()
