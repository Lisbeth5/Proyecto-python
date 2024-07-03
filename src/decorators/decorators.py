import time 
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def timeit(func):
    def wrapper(*args, **kwargs):
        tiempo_inicio = time.time() 
        resultado = func(*args, **kwargs)
        fin_de_tiempo = time.time()
        tiempo_transcurrido = fin_de_tiempo - tiempo_inicio
        logging.info(f"{func.__name__} ejecutada en {tiempo_transcurrido: 4f} seconds")

        return resultado
    return wrapper

def logit(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Corriendo {func.__name__}")
        resultado = func(*args, **kwargs)
        logging.info(f"Completado {func.__name__}")
        return resultado 
    return wrapper
