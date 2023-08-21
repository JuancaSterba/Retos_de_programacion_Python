"""
Reto #8: DECIMAL A BINARIO

Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""

def decimal_a_binario(decimal_num):
    if decimal_num == 0:
        return "0"
    
    resultado_binario = ""
    while decimal_num > 0:
        recordar = decimal_num % 2 # almacenamos el resto "0" o "1"
        resultado_binario = str(recordar) + resultado_binario # concatenamos el resultado a la cadena
        decimal_num //= 2 # dividimos por 2
    
    return resultado_binario

# Pedir al usuario un número decimal
decimal_input = int(input("Ingresa un número decimal: "))

# Convertir y mostrar el resultado en binario
binary_output = decimal_a_binario(decimal_input)
print(f"El número binario equivalente es: {binary_output}")
