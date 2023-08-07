"""
Reto #0: EL FAMOSO "FIZZ BUZZ”

Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 ==0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizz_buzz()


"""
Reto #1: ¿ES UN ANAGRAMA?

Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def anagrama(palabra1, palabra2):
    if palabra1.lower() == palabra2.lower():
        return False
    
    if sorted(palabra1.lower()) == sorted(palabra2.lower()):
        return True
    else:
        return False

resultado = anagrama("ramon","Ramon")
print(resultado)


"""
Reto #2: LA SUCESIÓN DE FIBONACCI

Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    anterior = 0
    siguiente = 1
    for i in range(0, 51):
        print(anterior)
        suma = anterior + siguiente
        anterior = siguiente
        siguiente = suma

fibonacci()


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

"""
Reto #4: ÁREA DE UN POLÍGONO
Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
"""

def area(*lados):
    if len(lados) == 1:
        lado = lados[0]
        area = lado ** 2
        print(f"El area del cuadrado es: {area}")
    elif len(lados) == 2:
        lado1 = lados[0]
        lado2 = lados[1]
        area = lado * lado2
        print(f"El area del rectángulo es: {area}")
    elif len(lados) == 3:
        lado1 = lados[0]
        lado2 = lados[1]
        lado3 = lados[2]
        s = (lado1 + lado2 + lado3)/2
        area = math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3)) # math esta importado mas arriba
        print(f"El area del triángulo es: {area}")
    else:
        print("El polígono no es válido")

area(3,4,5,6)
