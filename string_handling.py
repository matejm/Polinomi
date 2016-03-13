import Polinom

# Most of this can be done much better and nicer

def polinom_to_string(polinom):
    """
    >>> p = Polinom.Polinom([1,2,3])
    >>> p
    3x^2 + 2x + 1
    """
    if isinstance(polinom, Polinom.Polinom):
        polinom = polinom.coefficients
    s = []
    for i, j in list(enumerate(polinom))[::-1]:
        if j:
            if j == int(j): j = int(j)
            foo = ''
            if j == -1 and i != 0: foo += '-'
            elif j != 1 or i == 0: foo += str(j)
            if i:
                foo += 'x'
                if i != 1: foo += '^' + str(i)
            s.append(foo)
    if not s: s.append('0')
    out = s[0]
    for i in s[1:]:
        if i[0] == '-':
            out += ' - ' + i[1:]
        else:
            out += ' + ' + i
    return out

def string_to_polinom(string):
    """
    >>> string_to_polinom('x^2 + 2x + 3')
    [3, 2, 1]
    """
    string = string.replace(' ', '')
    if not string:
        return Polinom.Polinom([0])
    l = [0]
    while 'x' in string:
        index = string.find('x')
        if index > 0:
            try:
                coef = float(string[:index].replace('+',''))
            except:
                coef = -1 if '-' in string[:index] else 1
        else:
            coef = 1
        string = string[index+1:]
        stopnja = 1
        foo = ''
        if string and string[0] == '^':
            string = string[1:]
            while string and string[0].isdigit():
                foo += string[0]
                string = string[1:]
            stopnja = int(foo.replace('+',''))
        while stopnja >= len(l):
            l.append(0)
        l[stopnja] = coef
    if string:
        l[0] = float(string)
    l = [int(i) if int(i)==i else i for i in l]
    return l


if __name__ == '__main__':
    import doctest
    doctest.testmod()
