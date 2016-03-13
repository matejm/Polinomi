from Polinom import Polinom

def derivative(polinom):
    """
    >>> derivative(Polinom([1,2,3]))
    6x + 2
    """
    l = []
    for i in range(1, polinom.degree+1):
        l.append(polinom.coefficients[i]*i)
    return Polinom(l)

def horners_method(polinom, x):
    """
    >>> horners_method([-1,2,-6,2],3)
    ([2, 0, 2], 5)
    """
    result = 0
    polinom2 = []
    for c in polinom[::-1]:
        result = result * x + c
        polinom2.append(result)
    remainder, *polinom2 = reversed(polinom2)
    return polinom2, remainder

def get_divisors(n):
    """
    >>> get_divisors(10)
    [1, -1, 2, -2, 5, -5, 10, -10]
    """
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            divisors.append(i)
            divisors.append(-i)
            if i*i != n:
                divisors.append(n//i)
                divisors.append(-n//i)
    return sorted(divisors, key=abs)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
