def func(x):
    return x**2


def biseccion(func, a, b, Es, Ni):
    Ea = 100
    i = 1
    MActual = 0
    MPrevia = 0

    while (i < Ni) & (Ea > Es):
        MPrevia = MActual
        MActual = (a + b) / 2

        if func(MActual) * func(b) < 0:
            a = MActual
        else:
            b = MActual

        if i > 1:
            Ea = abs((MActual - MPrevia) / MActual) * 100

        i += 1
    print(MActual)
    print(Ea)
    print(i)


a = 1
b = 0
Es = 0.002
Ni = 8

biseccion(func, a, b, Es, Ni)
