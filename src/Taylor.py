import math
def taylor_polynomial(f, a, n):
    """
    Construye el polinomio de Taylor de orden n para la función f en el punto a.

    Parámetros:
    f (función): la función para la que se quiere construir el polinomio de Taylor
    a (número): el punto en el que se evalúa la función
    n (entero): el orden del polinomio de Taylor

    Retorna:
    Una lista de coeficientes del polinomio de Taylor
    """
    coeficientes = []
    for i in range(n + 1):
        coeficiente = f(a) / math.factorial(i)
        coeficientes.append(coeficiente)
        f1 = lambda x: (f(x) - coeficiente) / (x - a)
    return coeficientes



def df(f,h = 0.03):
    def w(x):
        return f(x + h) - f(x)/h
    return w

y = lambda x: pow(x,2) + math.cos(x)

print(taylor_polynomial(y,0,3))