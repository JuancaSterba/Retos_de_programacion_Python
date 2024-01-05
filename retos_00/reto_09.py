"""
Reto #9: CÓDIGO MORSE

Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
- Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
- En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
- El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
"""

codigo_morse = {
    ' ': ' ',
    'A': '·—',    
    'B': '—···',    
    'C': '—·—·',
    'D': '—··',    
    'E': '·',    
    'F': '··—·',    
    'G': '——·',
    'H': '····',    
    'I': '··',    
    'J': '·———',    
    'K': '—·—',
    'L': '·—··',    
    'M': '——',    
    'N': '—·',    
    'Ñ': '——·——',
    'O': '———',    
    'P': '·——·',    
    'Q': '——·—',    
    'R': '·—·',
    'S': '···',    
    'T': '—',    
    'U': '··—',    
    'V': '···—',
    'W': '·——',    
    'X': '—··—',    
    'Y': '—·——',    
    'Z': '——··',
    '0': '—————',    
    '1': '·————',    
    '2': '··———',    
    '3': '···——',
    '4': '····—',    
    '5': '·····',    
    '6': '—····',    
    '7': '——···',
    '8': '———··',    
    '9': '————·',    
    '.': '·—·—·—',    
    ',': '——··——'
}

def texto_a_morse(text):
    morse_text = ''
    for letra in text.upper():
        morse_letra = codigo_morse.get(letra, "")
        morse_text += morse_letra + ' ' #if morse_letra != ' ' else '  '
    return morse_text.strip()

def morse_a_texto(morse):
    palabras_en_texto = []
    letras = morse.split(' ')  # Separar por espacio para obtener letras
    
    palabra_texto = ''
    for letra in letras:
        if letra == '':
            palabras_en_texto.append(palabra_texto)
            palabra_texto = ''
            continue
        
        # Buscar la letra correspondiente en el diccionario codigo_morse
        for key, value in codigo_morse.items():
            if value == letra:
                palabra_texto += key
                break
    
    # Agregar la última palabra
    palabras_en_texto.append(palabra_texto)
    
    return ' '.join(palabras_en_texto)

def es_codigo_morse(texto):
    return '   ' in texto

texto_entrada = input("Ingrese el texto o código Morse: ")

if es_codigo_morse(texto_entrada):
    texto_convertido = morse_a_texto(texto_entrada)
    print("Código Morse convertido a texto:", texto_convertido)
else:
    morse_convertido = texto_a_morse(texto_entrada)
    print("Texto convertido a código Morse:", morse_convertido)
    