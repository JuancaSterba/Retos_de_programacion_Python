"""
#13
¿ES UN PALÍNDROMO?
Escribe una función que reciba un texto y retorne verdadero o
falso (Boolean) según sean o no palíndromos.
Un Palíndromo es una palabra o expresión que es igual si se lee
de izquierda a derecha que de derecha a izquierda.
NO se tienen en cuenta los espacios, signos de puntuación y tildes.
Ejemplo: Ana lleva al oso la avellana.
"""

import re

def textCleaner(texto: str) -> str:
  # Remueve todos los caracteres que no sean letras
  return re.sub("[^a-zA-Z]", "", texto).lower()

def textCleaner2(texto: str) -> str:
  # Remueve todos los caracteres que no sean letras sin usar expresiones regulares
  textoLimpio = ""
  for i in range(len(texto)):
    if texto[i].isalpha():
      textoLimpio += texto[i]
  return textoLimpio.lower()
  

def esPalindromo(texto: str) -> bool:
  # limpiamos el texto dejando solo letras
  texto = textCleaner(texto)
  # invertimos el texto
  textoInvertido = texto[::-1]
  print(textoInvertido)
  # comparamos el texto original con el invertido
  return texto == textoInvertido

def esPalindromo2(texto: str) -> bool:
  # limpiamos el texto dejando solo letras
  texto = textCleaner2(texto)
  # invertimos el texto sin funciones
  textoInvertido = ""
  for i in range(len(texto)-1, -1, -1):
    textoInvertido += texto[i]  
  # comparamos el texto original con el invertido
  return texto == textoInvertido

print(f"Es palindromo: {esPalindromo('Ana lleva al oso la avellana')}")
print(f"Es palindromo: {esPalindromo2("Ana lleva al oso la avellana")}")