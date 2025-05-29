from datetime import datetime
from dataclasses import dataclass

@dataclass
class Log:
    timestamp: datetime
    sala: str
    estado: str
    temperatura: float
    humedad: float
    co2: float
    mensaje: str

def parse_csv_logs(filepath):
    logs = []
    with open(filepath, 'r') as f:
        headers = f.readline().strip().split(',')
        for line in f:
            if not line.strip():
                continue
            fields = line.strip().split(',')
            try:
                data = dict(zip(headers, fields))
                log = Log(
                    timestamp=datetime.fromisoformat(data['timestamp']),
                    sala=data['sala'],
                    estado=data['estado'],
                    temperatura=float(data['temperatura']),
                    humedad=float(data['humedad']),
                    co2=float(data['co2']),
                    mensaje=data['mensaje']
                )
                logs.append(log)
            except Exception as e:
                print(f"Registro mal formado ignorado: {line.strip()} -> {e}")
    return logs
