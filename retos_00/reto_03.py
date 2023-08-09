"""
Reto #3: ¿ES UN NÚMERO PRIMO?

Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

import math

def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1): # comprobando la raiz cuadrada optimizamos la función
        if numero % i == 0:
            return False
    return True

for i in range(1, 101):
    if primo(i):
        print(i)
