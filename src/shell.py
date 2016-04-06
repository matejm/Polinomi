from Polinom import Polinom
from Fraction import Fraction
from GUI import GUI
from equation import solve, solve_poles
from inequation import solve_inequation
from numerical_methods import Bisection, Tangent, Secant, Iteration
from bisekcija import bisekcija

def graf(f):
    if isinstance(f, int) or isinstance(f, float):
        f = Polinom([f])
    if isinstance(f, Polinom):
        f = Fraction(f, 1)
    print('Ničle:', solve(f)[1])
    print('Poli: ', solve_poles(f)[1])
    print('Asimptota:', f.num//f.denum)
    print('Presečišča z asimptoto:', solve(f.num % f.denum))
    print('Začetna vrednost:', f[0])