"""
#12
CADENAS Y CARACTERES
/*
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 */
 """
 
def get_unique_caracters(str1: str, str2: str) -> str:
  out = ""
  for char in str1:
    if char not in str2:
      out += char
  return out

str1 = "Hello"
str2 = "World"

out1 = get_unique_caracters(str1, str2)
out2 = get_unique_caracters(str2, str1)

print(f"out1: {out1}")
print(f"out2: {out2}")
