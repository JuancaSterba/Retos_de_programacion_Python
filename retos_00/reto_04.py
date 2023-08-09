"""
Reto #4: ÁREA DE UN POLÍGONO
Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
"""

import math


def area(*lados):
    if len(lados) == 1:
        lado = lados[0]
        area = lado ** 2
        print(f"El area del cuadrado es: {area}")
    elif len(lados) == 2:
        lado1 = lados[0]
        lado2 = lados[1]
        area = lado1 * lado2
        print(f"El area del rectángulo es: {area}")
    elif len(lados) == 3:
        lado1 = lados[0]
        lado2 = lados[1]
        lado3 = lados[2]
        s = (lado1 + lado2 + lado3)/2
        area = math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3)) # math esta importado mas arriba, se utiliza fórmula de Herón
        print(f"El area del triángulo es: {area}")
    else:
        print("El polígono no es válido")

area(5, 4, 7)
