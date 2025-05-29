class ConsoleDecorator:
    def __init__(self, reporte):
        self.reporte = reporte

    def mostrar(self):
        print("🔷 Mostrando reporte:")
        self.reporte.calcular()
        print(self.reporte.obtener_datos())
        print("-" * 50)
