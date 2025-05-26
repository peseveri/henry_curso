import pandas as pd

def export_to_csv(df, path):
    df.to_csv(path, index=False)
    print(f"✅ Reporte exportado a CSV: {path}")

def export_to_excel(df, path):
    df.to_excel(path, index=False)
    print(f"✅ Reporte exportado a Excel: {path}")
