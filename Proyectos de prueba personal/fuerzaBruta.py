#funcion que adivina la contraseña usando fuerza bruta

import string, itertools


def fuerza_bruta(contrasena):
    caracteres = string.ascii_letters + string.digits
    intentos = 0
    print("Adivinando la contraseña...")
    for longitud in range(1, len(contrasena) + 1):
        for intento in map(''.join, itertools.product(caracteres, repeat=longitud)):
            intentos += 1
            if intento == contrasena:
                print(f"Se adivino la contraseña en {intentos} intentos.")
                print(f"Se ha tardado {intentos} intentos.")
                return
    print("No se pudo adivinar la contraseña.")

contrasena = input("Ingrese la contraseña a adivinar: ")
fuerza_bruta(contrasena)