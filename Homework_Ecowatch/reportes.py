import pandas as pd
from abc import ABC, abstractmethod

class ReportStrategy(ABC):
    @abstractmethod
    def generate(self, logs):
        pass

class EstadoPorSalaStrategy(ReportStrategy):
    def generate(self, logs):
        # Convertir lista de logs a DataFrame
        df = pd.DataFrame([{
            'timestamp': log.timestamp,
            'sala': log.sala,
            'estado': log.estado,
            'temperatura': log.temperatura,
            'humedad': log.humedad,
            'co2': log.co2,
            'mensaje': log.mensaje

        } for log in logs])
        # Agrupar por sala y calcular medias
        resumen = df.groupby('sala').agg({
            'temperatura': 'mean',
            'humedad': 'mean',
            'co2': 'mean'
        }).reset_index()
        return resumen

class AlertasCriticasStrategy(ReportStrategy):
    def generate(self, logs):
        df = pd.DataFrame([{
            'timestamp': log.timestamp,
            'sala': log.sala,
            'temperatura': log.temperatura,
            'humedad': log.humedad,
            'co2': log.co2,
            'estado': log.estado,
            'mensaje': log.mensaje
        } for log in logs])
        # Filtrar alertas críticas
        alertas = df[(df['estado'] == 'WARNING') | (df['co2'] > 1000)]
        return alertas

# Decorator para convertir DataFrame a texto simple
class ReportDecorator(ReportStrategy):
    def __init__(self, report_strategy):
        self._report_strategy = report_strategy

    def generate(self, logs):
        return self._report_strategy.generate(logs)


class DataFrameToCSVDecorator(ReportDecorator):
    def generate(self, logs):
        df = self._report_strategy.generate(logs)
        resumen = self._crear_resumen(df)
        self._exportar_csv(df)
        return {'data': df, 'resumen': resumen}

    def _crear_resumen(self, df):
        return df.to_string(index=False)

    def _exportar_csv(self, df):
        filename = f'reporte_estado_por_sala.csv'
        df.to_csv(filename, index=False)
        print(f"📁 Reporte exportado como CSV: {filename}")

class DataFrameToXLSXDecorator(ReportDecorator):
    def generate(self, logs):
        df = self._report_strategy.generate(logs)
        resumen = self._crear_resumen(df)
        self._exportar_xlsx(df)
        return {'data': df, 'resumen': resumen}

    def _crear_resumen(self, df):
        return df.to_string(index=False)

    def _exportar_xlsx(self, df):
        filename = f'reporte_alertas_criticas.xlsx'
        df.to_excel(filename, index=False)
        print(f"📁 Reporte exportado como XLSX: {filename}")

class ReportFactory:
    strategies = {
        'estado_por_sala': EstadoPorSalaStrategy,
        'alertas_criticas': AlertasCriticasStrategy
    }

    decorators = {
        'csv': DataFrameToCSVDecorator,
        'xlsx': DataFrameToXLSXDecorator
    }

    @classmethod
    def create_report(cls, tipo, decorator=None):
        strategy_cls = cls.strategies.get(tipo)
        if not strategy_cls:
            raise ValueError(f"Tipo de reporte desconocido: {tipo}")
        strategy = strategy_cls()

        if decorator:
            decorator_cls = cls.decorators.get(decorator)
            if not decorator_cls:
                raise ValueError(f"Decorator desconocido: {decorator}")
            return decorator_cls(strategy)
        return strategy
