import math


def derivada(funcion, x):
    """
    Calcula la derivada de una función en un punto.
    """

    h = 0.0001
    return (funcion(x + h) - funcion(x)) / h


def max_min_en_intervalo(funcion, a, b):
    """
    Encuentra el máximo y mínimo de una función en un intervalo cerrado [a, b].
    """
    puntos_criticos = []
    for x in range(a, b + 1):
        if derivada(funcion, x) == 0 or math.isnan(derivada(funcion, x)):
            puntos_criticos.append(x)

    # Se evalúa la función en los puntos críticos y en los extremos del intervalo
    valores_funcion = [funcion(x) for x in puntos_criticos]
    valores_funcion.append(funcion(a))
    valores_funcion.append(funcion(b))

    # Se encuentra el máximo y mínimo
    maximo = max(valores_funcion)
    minimo = min(valores_funcion)

    return {"maximo": maximo, "minimo": minimo}


# para dar un ejemplo, se crea una variable funcion que tendra la funcion que desea operar
funcion = lambda x: x**3 - 3 * x**2 + 2 * x
intervalo = [0, 2]

resultado = max_min_en_intervalo(funcion, intervalo[0], intervalo[1])

print(f"Función: f(x) = x^3 - 3x^2 + 2x")
print(f"Intervalo: [{intervalo[0]}, {intervalo[1]}]")
print(f"Máximo: {resultado['maximo']}")
print(f"Mínimo: {resultado['minimo']}")
