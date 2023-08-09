"""
Reto #6: INVIRTIENDO CADENAS

Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def inversor(texto):
  texto_invertido = ""
  for caracter in texto:
    texto_invertido = caracter + texto_invertido
  return texto_invertido

texto = input("Ingrese un texto: ")
resultado = inversor(texto)
print("Texto invertido: " + resultado)
