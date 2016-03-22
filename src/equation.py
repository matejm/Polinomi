from Polinom import Polinom
import Fraction
from methods import horners_method, get_divisors
import cmath


def solve_linear(polinom):
    """
    >>> solve_linear([3,5])
    -0.6
    """
    b, a = polinom
    c = -b/a
    if c == int(c): c = int(c)
    return c

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

def solve_quartic(polinom):
    """
    >>> solve_quartic([1,1,1,1,1])
    ((-0.809017-0.5877853j), (-0.809017+0.5877853j), (0.309017-0.9510565j), (0.309017+0.9510565j))
    """
    a, b, c, d, e = polinom
    p1 = 2*c**3 - 9*b*c*d + 27*a*d**2 + 27*b**2*e - 72*a*c*e
    p2 = p1 + cmath.sqrt(-4*(c**2 - 3*b*d + 12*a*e)**3 + p1**2)
    p3 = (c**2 - 3*b*d + 12*a*e) / (3*a * pow(p2/2, 1/3)) + pow(p2/2, 1/3) / (3*a)
    p4 = cmath.sqrt((b**2)/(4*a**2) - (2*c)/(3*a) + p3)
    p5 = (b**2) / (2*a**2) - (4*c) / (3*a) - p3
    p6 = ((-b**3)/(a**3) + (4*b*c)/(a**2) - (8*d)/a) / (4*p4)
    x = [0]*4
    x[0] = -b/(4*a) - p4/2 - cmath.sqrt(p5 - p6)/2
    x[1] = -b/(4*a) - p4/2 + cmath.sqrt(p5 - p6)/2
    x[2] = -b/(4*a) + p4/2 - cmath.sqrt(p5 + p6)/2
    x[3] = -b/(4*a) + p4/2 + cmath.sqrt(p5 + p6)/2
    for i in range(4):
        x[i] = complex(round(x[i].real, 7), round(x[i].imag, 7))
        if not x[i].imag:
            x[i] = x[i].real
            if x[i] == int(x[i]): x[i] = int(x[i])
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
    if isinstance(polinom, Fraction.Fraction):
        polinom = polinom.num
    if isinstance(polinom, Polinom):
        polinom = polinom.coefficients
    l = len(polinom)
    if l == 0:
        polinom.append(0)
        l += 1
    if l == 1:
        if polinom[0] == 0:
            return -1, tuple()
        else:
            return 0, tuple()
    if l == 2:
        return 1, (solve_linear(polinom),)
    if all([i == int(i) for i in polinom]):
        c = get_divisors(polinom[0]) + [0]
        d = get_divisors(polinom[-1])
        candidats = set()
        for num in c:
            for denum in d:
                frac = num/denum
                if frac == int(frac): frac = int(frac)
                candidats.add(frac)
        for can in candidats:
            polinom2, remainder = horners_method(polinom, can)
            if not remainder:
                number, solutions = solve_equation(polinom2)
                if number != -2: number += 1
                return number, tuple(list(solutions)+[can])
    if l == 3:
        return 2, solve_quadratic(polinom)
    elif l == 4:
        return 3, solve_cubic(polinom)
    elif l == 5:
        return 4, solve_quartic(polinom)
    return -2, ()

solve = solve_equation

if __name__ == '__main__':
    import doctest
    doctest.testmod()
