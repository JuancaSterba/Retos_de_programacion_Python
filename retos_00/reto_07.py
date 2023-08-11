"""
Reto #7: CONTANDO PALABRAS

Crea un programa que cuente cuantas veces se repite cada palabra
y que muestre el recuento final de todas ellas.
- Los signos de puntuación no forman parte de la palabra.
- Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
- No se pueden utilizar funciones propias del lenguaje que
  lo resuelvan automáticamente.

"""

def cuenta_palabras(texto):
  texto = texto.lower()
  texto = texto.replace(".", "").replace(",", "").replace(":", "").replace(";","")
  palabras = texto.split()
  dicc = {}
  for palabra in palabras:
      if palabra in dicc:
          dicc[palabra] += 1
      else:
          dicc[palabra] = 1
  return dicc  

texto = "Python es un lenguaje de programación de propósito general, de uso común, y de código abierto."

print(cuenta_palabras(texto))