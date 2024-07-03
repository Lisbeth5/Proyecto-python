import requests
from bs4 import BeautifulSoup
import pandas as pd

def obtener_data_pagina(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to fetch page: {url}")

def analizar_producto(producto):
    descripcion = producto.select_one(".product-title").text.strip() if producto.select_one(".product-title") else None
    # Extraer el precio y eliminar etiquetas HTML
    precio = producto.select_one(".old-price")
    precio = precio.text.strip() if precio else None
    # Extraer el porcentaje de descuento y eliminar etiquetas HTML
    porcentaje_descuento = producto.select_one(".label.sale-label")
    porcentaje_descuento = porcentaje_descuento.text.strip() if porcentaje_descuento else None
    
    return {
        "descripcion": descripcion,
        "precio": precio,
        "porcentaje": porcentaje_descuento
    }

def scraping_data(url):
    contenido_pagina = obtener_data_pagina(url)
    soup = BeautifulSoup(contenido_pagina, "html.parser")
    productos = soup.find_all("div", class_="inner product-item on-sale")
    
    guardar_productos = []

    for producto in productos:
        informacion_producto = analizar_producto(producto)
        guardar_productos.append(informacion_producto)
    
    return pd.DataFrame(guardar_productos)

url = "https://www.lvxo.ec/"
df = scraping_data(url)

print(df)
df.to_csv("data/raw/Productos.csv", index=False)
