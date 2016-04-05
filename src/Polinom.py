import string_handling

class Polinom:
    """
    Each polynomial is represented as a list of coefficients.
    p(x) = Anx^n + .... + A2x^2 + A1x + A0
    i-th element of a list represents coefficient Ai
    """
    def __init__(self, data):
        """
        >>> p = Polinom([1,2,3])
        >>> p = Polinom('3x^2 + 2x + 1')
        """
        if isinstance(data, str):
            data = string_handling.string_to_polinom(data)
        self.coefficients = self._erase_zeroes(data)
        self.degree = len(self.coefficients) - 1

    @staticmethod
    def _erase_zeroes(list):
        """
        >>> Polinom._erase_zeroes([0,1,0])
        [0, 1]
        """
        b = True
        for i in list:
            if i: b = False
        if b:
            return [0]
        if len(list) > 1 and list[-1] == 0:
            i =- 1
            while len(list) > 1 and list[i] == 0:
                i -= 1
            list = list[:i+1]
        return list

    @staticmethod
    def _add(p1, p2):
        px = [0] * min(len(p1),len(p2))
        i = 0
        for i in range(len(px)):
            px[i] = p1[i] + p2[i]
        px += p1[i+1:] + p2[i+1:]
        return px

    @staticmethod
    def _mul(p1, p2):
        px = [0] * (len(p1) + len(p2))
        for i in range(len(p1)):
            for j in range(len(p2)):
                px[i+j] += p1[i] * p2[j]
        return px

    def _div(self, p1, p2):
        if len(p1) < len(p2): return [0], p1

        x = len(p1) - len(p2)   # difference between degrees
        p2 = [0] * x + p2       # shift p2 coefficients
        px = []                 # quotionet
        d = p2[-1]
        for i in range(x+1):
            res = p1[-1] / d    # division of coefficients
            px = [res] + px
            if res != 0:
                sub_me = [res*i for i in p2]
                p1 = [i - j for i, j in zip(p1, sub_me)]
            p1.pop()
            p2.pop(0)

        remainder = self._erase_zeroes(p1)
        return px, remainder

    def __neg__(self):
        """
        >>> -Polinom([1,2,3])
        -3x^2 - 2x - 1
        """
        return Polinom([-i for i in self.coefficients])

    def __add__(self, other):
        """
        >>> p = Polinom([1,2,3])
        >>> p + 2
        3x^2 + 2x + 3
        >>> q = Polinom([4,5,6])
        >>> p + q
        9x^2 + 7x + 5
        """
        if isinstance(other, Polinom):
            return Polinom(self._add(self.coefficients, other.coefficients))
        if isinstance(other, float) or isinstance(other, int):
            list = self.coefficients[:]    # copy
            list[0] += other
            return Polinom(list)
        raise TypeError('Invalid operation for Polinom and '+type(other).__name__)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        """
        >>> p = Polinom([1,2])
        >>> p * 2
        4x + 2
        >>> q = Polinom([0,1,3])
        >>> p * q
        6x^3 + 5x^2 + x
        """
        if isinstance(other, Polinom):
            return Polinom(self._mul(self.coefficients, other.coefficients))
        if isinstance(other, float) or isinstance(other, int):
            list = [i * other for i in self.coefficients]
            return Polinom(list)
        raise TypeError('Invalid operation for Polinom and '+type(other).__name__)

    def __truediv__(self, other):
        """
        >>> p = Polinom([-3, -3, 1, 1])
        >>> p / 2
        0.5x^3 + 0.5x^2 - 1.5x - 1.5
        >>> q = Polinom([-4, 1])
        >>> p / q
        (x^2 + 5x + 17, 65)
        """
        if isinstance(other, Polinom):
            if other.degree == 0:
               other = other.p[0]
            else:
                res, remainder = self._div(self.coefficients, other.coefficients)
                return Polinom(res), Polinom(remainder)
        if isinstance(other, float) or isinstance(other, int):
            list = [i/other for i in self.coefficients]
            return Polinom(list)
        raise TypeError('Invalid operation for Polinom and '+type(other).__name__)

    def __floordiv__(self, other):
        if isinstance(other, Polinom):
            return Polinom(self._div(self.coefficients, other.coefficients)[0])
        if isinstance(other, float) or isinstance(other, int):
            list = [i//other for i in self.coefficients]
            return Polinom(list)
        raise TypeError('Invalid operation for Polinom and '+type(other).__name__)

    def __mod__(self, other):
        if isinstance(other, Polinom):
            return Polinom(self._div(self.coefficients, other.coefficients)[1])
        raise TypeError('Invalid operation for Polinom and '+type(other).__name__)

    def __eq__(self, other):
        """
        >>> Polinom('x + 1') == Polinom([1, 1])
        True
        """
        if isinstance(other, Polinom):
            return self.coefficients == other.coefficients
        return False

    def __repr__(self):
        return string_handling.polinom_to_string(self.coefficients)

    def __getitem__(self, x):
        res = 0
        for i, c in enumerate(self.coefficients):
            res += c*x**i
        return res

    value = __getitem__


if __name__ == '__main__':
    import doctest
    doctest.testmod()
