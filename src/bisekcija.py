def bisekcija(a, b, polinom):
    v = -1
    
    if polinom[a] < 0:
        a, b = b, a

    while abs(v) > 10**(-8):
        c = (a+b)/2
        v = polinom[c]
        if v > 0: a = c
        else: b = c
        
        print('vrednost: {:.8f}\t\t{:.8f} < x < {:.8f}'.format(v, a, b))

    return c