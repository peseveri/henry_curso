from dotenv import load_dotenv
import os
from logs import parse_csv_logs
from cache import TemporalCache
from datetime import datetime
from utils import (
    esperar_expiracion_cache,
    consultar_logs,
    generar_reportes
)


def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Esperar 5 minutos y limpieza del cache")
    print("2. Consultar logs por sala o timestamp")
    print("3. Generar reportes")
    print("0. Salir")
    return input("Elige una opción: ")

def main():
    load_dotenv()
    data_source = os.getenv('DATA_SOURCE', 'logs_ambientales_ecowatch.csv')
    cache_duration = int(os.getenv('CACHE_DURATION_MINUTES', 5))

    logs = parse_csv_logs(data_source)
    cache = TemporalCache(window_minutes=cache_duration)

    for log in logs:
        cache.add_log(log)

    init_time = datetime.now()
    print(f"Logs cargados en cache ({len(cache.get_all_logs())}) a las {init_time.strftime('%H:%M:%S')}")

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            esperar_expiracion_cache(cache, cache_duration,init_time)
        elif opcion == "2":
            consultar_logs(cache)
        elif opcion == "3":
            generar_reportes(cache)
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    main()
