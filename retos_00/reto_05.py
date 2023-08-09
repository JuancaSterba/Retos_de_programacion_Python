"""
Reto #5: ASPECT RATIO DE UNA IMAGEN

Crea un programa que se encargue de calcular el aspect ratio de una
imagen a partir de una url.
- Url de ejemplo: https://raw.githubusercontent.com/mouredev/
  mouredev/master/mouredev_github_profile.png
- Por ratio hacemos referencia por ejemplo a los "16:9" de una
  imagen de 1920*1080px.

"""

import requests
from PIL import Image
from io import BytesIO

def mcd(a, b): # Hallamos el máximo común divisor
    while b:
        a, b = b, a % b
    return a

def format_aspect_ratio(width, height): # Formateamos el valor de la relación de aspecto
    mcd_value = mcd(width, height)
    formatted_ratio = f"{int(width/mcd_value)}:{int(height/mcd_value)}"
    return formatted_ratio

def aspect_ratio(url):
    r = requests.get(url)

    if r.status_code == 200:
        img = Image.open(BytesIO(r.content))
        width, height = img.size
        # ratio = width / height
        formatted_ratio = format_aspect_ratio(width, height)
        
        print(f"Datos de la imagen:")
        print(f"Ancho: {width}")
        print(f"Alto: {height}")
        print(f"Relación de aspecto: {formatted_ratio}")
        
        # return formatted_ratio

aspect_ratio("https://cdn.appuals.com/wp-content/uploads/2021/12/1920x1080.png.webp")
