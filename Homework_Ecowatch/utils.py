from datetime import datetime, timedelta
from logs import Log 
import time
from reportes import ReportFactory

def generar_logs_prueba(cache, sala='Sala_3', cantidad=3):
    """
    Agrega logs de prueba con timestamps recientes en la cache,
    para la sala indicada y la cantidad deseada.
    """
    now = datetime.now()
    for i in range(cantidad):
        log_prueba = Log(
            timestamp=now - timedelta(seconds=i*10),  # Espaciados 10 seg
            sala=sala,
            estado='TEST',
            temperatura=22.5 + i,
            humedad=45 + i,
            co2=800 + i*10,
            mensaje='Log de prueba'
        )
        cache.add_log(log_prueba)

def esperar_expiracion_cache(cache, cache_duration, init_time):
    tiempo_transcurrido = (datetime.now() - init_time).total_seconds()
    tiempo_espera = cache_duration * 60 - tiempo_transcurrido

    print(f"Logs en cache antes de esperar: {len(cache.get_all_logs())}")

    if tiempo_espera > 0:
        minutos = int(tiempo_espera // 60)
        segundos = int(tiempo_espera % 60)
        print(f"Esperando {minutos} minutos y {segundos} segundos para que la cache expire...")
        time.sleep(tiempo_espera + 1)
    else:
        print("La cache ya debería haber expirado, no se espera.")

    generar_logs_prueba(cache, sala='Sala_3', cantidad=3)

    print(f"Logs en cache luego de la espera y nuevos logs ({len(cache.get_all_logs())}) a las {datetime.now().strftime('%H:%M:%S')}")


def consultar_logs(cache):
    tipo = input("Consultar por (1) Sala o (2) Timestamp: ")

    if tipo == "1":
        sala = input("Nombre de la sala: ")
        logs = cache.query_by_sala(sala)
    elif tipo == "2":
        timestamp_str = input("Timestamp exacto (YYYY-MM-DD HH:MM:SS): ")
        try:
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            logs = cache.query_by_timestamp(timestamp)
        except ValueError:
            print("Formato de fecha incorrecto.")
            return
    else:
        print("Opción inválida.")
        return

    print(f"Se encontraron {len(logs)} logs.")
    for log in logs:
        print(log)


def generar_reportes(cache):
    logs = cache.get_all_logs()

    print("\nGenerando reporte de estado por sala (se exportará a CSV)...")
    reporte_estado = ReportFactory.create_report('estado_por_sala', decorator='csv')
    reporte_estado.generate(logs)

    print("\nGenerando reporte de alertas críticas (se exportará a XLSX)...")
    reporte_alertas = ReportFactory.create_report('alertas_criticas', decorator='xlsx')
    reporte_alertas.generate(logs)
