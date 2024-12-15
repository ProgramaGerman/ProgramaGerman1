from functools import reduce

lista = [3, 4, 5, 6, 7, 8, 20, 12,21, 14]

# Usar reduce con una función lambda para encontrar el mayor elemento
mayor = reduce(lambda x, y: x if x > y else y, lista)

# Imprimir el mayor elemento
print(mayor)
