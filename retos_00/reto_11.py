"""
#11
EXPRESIONES EQUILIBRADAS
/*
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 */
"""

def is_balanced(expression: str) -> bool:
    symbols: dict = {"{": "}", "[": "]", "(": ")"}
    stack: list = []

    for symbol in expression:
        if symbol in symbols:
            stack.append(symbol)
        elif symbol in symbols.values():
            if not stack or symbol != symbols[stack.pop()]:
                return False

    return not stack

print("Es balanceada" if is_balanced("{a + b [c] * (2x2)}}}}") else "No es balanceada")
print("Es balanceada" if is_balanced("{ [ a * ( c + d ) ] - 5 }") else "No es balanceada")
print("Es balanceada" if is_balanced("{ a * ( c + d ) ] - 5 }") else "No es balanceada")
print("Es balanceada" if is_balanced("{a^4 + (((ax4)}") else "No es balanceada")
print("Es balanceada" if is_balanced("{ ] a * ( c + d ) + ( 2 - 3 )[ - 5 }") else "No es balanceada")
print("Es balanceada" if is_balanced("{{{{(){{()}}}[]}}}") else "No es balanceada")
print("Es balanceada" if is_balanced("(a") else "No es balanceada")
