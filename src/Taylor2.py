def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def derivada(funcion, x, orden):
    h = 1e-5
    if orden == 0:
        return funcion(x)
    elif orden == 1:
        return (funcion(x + h) - funcion(x - h)) / (2 * h)
    else:
        return (derivada(funcion, x + h, orden - 1) - derivada(funcion, x - h, orden - 1)) / (2 * h)

def polinomio_taylor(funcion, x0, grado):
    def taylor(x):
        suma = 0
        for i in range(grado + 1):
            termino = (derivada(funcion, x0, i) / factorial(i)) * ((x - x0) ** i)
            suma += termino
        return suma
    return taylor

# Ejemplo de uso
import math
funcion = math.sin  # Puedes cambiar esta función por la que desees
x0 = 0  # Punto alrededor del cual se expande el polinomio
grado = 5  # Grado del polinomio de Taylor

taylor = polinomio_taylor(funcion, x0, grado)
print(taylor(0.5))  # Evalúa el polinomio de Taylor en x = 0.5
