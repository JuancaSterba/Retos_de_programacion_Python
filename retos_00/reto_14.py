"""
#14
FACTORIAL RECURSIVO
Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
"""

def factorial (n: int) -> int:
  if n <= 1:
    return 1
  else:
    return n * factorial(n-1)
  
print(factorial(5))
