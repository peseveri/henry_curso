import ast
import pandas as pd
from factories import ReportFactory
from decorators import ConsoleDecorator
from utils import export_to_csv, export_to_excel

# Leer archivo
with open('datos_ventas.txt', 'r', encoding='utf-8') as file:
    raw_data = file.read()

inicio = raw_data.find('=') + 1
lista_texto = raw_data[inicio:].strip()

# Convertir string a objeto Python
datos_ventas = ast.literal_eval(lista_texto)

# Crear DataFrame
df = pd.DataFrame(datos_ventas)

# Crear y mostrar reportes
reportes = [
    ReportFactory.create_report("ventas_por_categoria", df),
    ReportFactory.create_report("resumen_por_categoria", df)
]

for reporte in reportes:
    decorado = ConsoleDecorator(reporte)
    decorado.mostrar()

# Exportación
export_to_csv(reportes[0].obtener_datos(), "output/ventas_por_categoria.csv")
export_to_excel(reportes[1].obtener_datos(), "output/resumen_por_categoria.xlsx")
