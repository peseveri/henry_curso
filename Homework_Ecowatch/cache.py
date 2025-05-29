from collections import defaultdict, deque
from datetime import datetime, timedelta

class TemporalCache:
    def __init__(self, window_minutes=5):
        self.window = timedelta(minutes=window_minutes)
        self.logs = deque()  # Cada ítem será (log, hora_agregado)
        self.by_sala = defaultdict(deque)

    def add_log(self, log):
        ahora = datetime.now()
        # Agrega (log, hora_agregado)
        self.logs.append((log, ahora))
        self.by_sala[log.sala].append((log, ahora))
        self._clean_old(ahora)

    def _clean_old(self, ahora):
        limite = ahora - self.window
        while self.logs and self.logs[0][1] < limite:
            viejo_log, _ = self.logs.popleft()
            sala_logs = self.by_sala[viejo_log.sala]
            if sala_logs and sala_logs[0][0].timestamp == viejo_log.timestamp:
                sala_logs.popleft()
            if not sala_logs:
                del self.by_sala[viejo_log.sala]

    def query_by_sala(self, sala):
        sala_str = str(sala)
        if sala_str.isdigit():
            sala_str = f"Sala_{sala_str}"
        return list(self.by_sala.get(sala_str, []))

    def query_by_timestamp(self, timestamp):
        return [log for log, _ in self.logs if log.timestamp == timestamp]

    def get_all_logs(self):
        return [log for log, _ in self.logs]
