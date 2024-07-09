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
        coefficient = f(a) / math.factorial(i)
        coeficientes.append(coefficient)
        f = lambda x: (f(x) - coefficient) / (x - a)
    return coeficientes

f = lambda x: math.sin(x)-x

taylor_polynomial(f,0,2)

