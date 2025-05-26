from strategies import TotalVentasPorCategoria, ResumenPorCategoria

class ReportFactory:
    @staticmethod
    def create_report(tipo, dataframe):
        if tipo == "ventas_por_categoria":
            return TotalVentasPorCategoria(dataframe)
        elif tipo == "resumen_por_categoria":
            return ResumenPorCategoria(dataframe)
        else:
            raise ValueError(f"Tipo de reporte desconocido: {tipo}")
