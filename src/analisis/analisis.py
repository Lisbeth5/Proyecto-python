import pandas as pd 
import os 
from ..decorators.decorators import timeit, logit


@logit 
@timeit
def cargar_datos(ruta_de_datos):
    if ruta_de_datos.endswith('.csv'):
        df = pd.read_csv(ruta_de_datos)
    elif ruta_de_datos.endswith('.xlsx'):
        df = pd.read_excel(ruta_de_datos)
    else:
        raise ValueError("Archivo de formato no valido")
    print("Datos cargados exitosamente")
    return df

print(cargar_datos("data/raw/Productos.csv"))


@logit
@timeit
def limpia_datos(df):
    df['precio'] = df['precio'].replace(r'[\$]', '', regex=True).astype(float)
    df['porcentaje'] = df['porcentaje'].fillna(0).replace(r'[%\-]', '', regex=True).astype(int)
    print("Datos limpios correctamente")
    return df
#
#
@logit
@timeit
def analizar_datos(df):
    print("Analisis de datos basicos:")
    print(df.describe())
    print("\nProductos con precios altos:")
    highestPrices = df.nlargest(5, 'precio')
    print(highestPrices)


@logit
@timeit
def guarda_datos_limpios(df, ruta_salida_datos):
    if ruta_salida_datos.endswith('.csv'):
        df.to_csv(ruta_salida_datos, index=False)
    elif ruta_salida_datos.endswith('.xlsx'):
        df.to_excel(ruta_salida_datos, index=False)
    else:
        raise ValueError("Formato de archivo no soportado")
    print(f"Limpiar datos guardados en {ruta_salida_datos}")



if __name__ == "__main__":
    ruta_de_datos = "data/raw/Productos.csv"
    ruta_salida_de_datos = "data/processed/Productos_limpios.csv"

    df = cargar_datos(ruta_de_datos)
    df = limpia_datos(df)
    analizar_datos(df)
    os.makedirs("data/processed", exist_ok=True)
    guarda_datos_limpios(df, ruta_salida_de_datos)
