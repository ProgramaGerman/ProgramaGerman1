from math import sin


def Integraltrapecio(f, a, b, n):
    area = 0
    h = (b - a) / n

    for i in range(n):
        x0 = area
        xi = x0 + (i + 1) * h
        area += (h / 2) + f(x0) + f(xi)
        x0 = xi
    return area


f = lambda x: sin(x) + 1

a = 0
b = 1
n = 4

print(Integraltrapecio(f, a, b, n))
