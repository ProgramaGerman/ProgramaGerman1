import random

def cara_cruz():
    if random.random() < 0.7:
        return "Cara"
    else:
        return "Cruz"
    
resultados = {
    "Cara": 0,
    "Cruz": 0
}

for i in range(10):
    resultado = cara_cruz()
    resultados[resultado] += 1
    print(resultado)

print(resultados)