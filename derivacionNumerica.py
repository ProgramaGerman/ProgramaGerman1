from math import sin

fx = lambda x: sin(x) - x


def dx2(fx, x0, h=0.02):
    def w(x0):
        return fx(x0 + h) - fx(x0 - h) / 2 * h

    return w


def dx(fx, x, h=0.02):
    return fx(x + h) - fx(x - h) / 2 * h


df = dx(fx, 1)
print(dx2(df, 1))
