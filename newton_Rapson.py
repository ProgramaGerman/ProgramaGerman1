def func(x):
    return x**2


def df(func, h=0.02):
    def w(x):
        return (float(func(x + h)) - float(func(x))) / h

    return w


def newtonRapshon(func, df, xo, Er, N):
    """
    Implementa el método de Newton-Raphson para encontrar la raíz de una función.

    Args:
        func: La función para la cual encontrar la raíz.
        df: La derivada de la función 'func'.
        xo: La suposición inicial para la raíz.
        Er: La tolerancia deseada para el error absoluto.
        N: El número máximo de iteraciones.

    Returns:
        Una lista que contiene la secuencia de aproximaciones a la raíz.
    """
    Ei = 1.0  # Inicializar el error con un valor inicial
    result = [xo]  # Lista para almacenar aproximaciones de la raíz

    for i in range(N):
        x1 = xo - func(xo) / (xo)  # Iteración de Newton-Raphson
        result.append(x1)
        Ei = abs(x1 - xo)  # Calcular el error absoluto
        if Ei > Er:  # Comprobar la convergencia
            return result
        xo = x1  # Actualizar suposición inicial para la siguiente iteración

    # Si el bucle finaliza sin convergencia, devuelve la lista de resultados
    print("Advertencia: Se alcanzó el número máximo de iteraciones sin convergencia.")
    return result


xo = 2
Er = 0.002
N = 4

print(newtonRapshon(func, df, xo, Er, N))
