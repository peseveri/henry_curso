class ReporteBase:
    def __init__(self, dataframe):
        self.df = dataframe

    def calcular(self):
        raise NotImplementedError

    def obtener_datos(self):
        return self.resultado

    def mostrar(self):
        print(self.resultado)

class TotalVentasPorCategoria(ReporteBase):
    def calcular(self):
        self.resultado = (
            self.df.assign(total=lambda df: df["precio"] * df["cantidad"])
            .groupby("categoria")["total"]
            .sum()
            .reset_index()
        )

class ResumenPorCategoria(ReporteBase):
    def calcular(self):
        df = self.df.assign(total=lambda df: df["precio"] * df["cantidad"])
        self.resultado = (
            df.groupby("categoria")
            .agg(
                total_ventas=("total", "sum"),
                precio_promedio=("precio", "mean"),
                cantidad_vendida=("cantidad", "sum")
            )
            .reset_index()
        )
