import pandas as pd
import matplotlib.pyplot as plt

# Se lee el archivo CSV ubicado en la carpeta datos.
# Usamos una ruta relativa para que funcione correctamente en Google Colab.
df = pd.read_csv("datos/ventas.csv")

# Se calcula el total vendido en cada venta.
df["total"] = df["cantidad"] * df["precio"]

# Se calcula el total general de ventas.
ventas_totales = df["total"].sum()

# Se identifica el producto más vendido según la cantidad total.
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()

# Se convierte la columna fecha a formato de fecha.
df["fecha"] = pd.to_datetime(df["fecha"])

# Se crea una columna con el mes de cada venta.
df["mes"] = df["fecha"].dt.to_period("M").astype(str)

# Se calculan las ventas totales por mes.
ventas_por_mes = df.groupby("mes")["total"].sum()

# Se guarda un resumen de los resultados en la carpeta resultados.
with open("resultados/resumen_ventas.txt", "w", encoding="utf-8") as archivo:
    archivo.write(f"Ventas totales: ${ventas_totales}\n")
    archivo.write(f"Producto más vendido: {producto_mas_vendido}\n")
    archivo.write("\nVentas por mes:\n")
    archivo.write(ventas_por_mes.to_string())

# Se genera un gráfico simple de ventas por mes.
ventas_por_mes.plot(kind="bar", title="Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Total vendido")
plt.tight_layout()

# Se guarda el gráfico en la carpeta resultados.
plt.savefig("resultados/grafico_ventas.png")

print("Análisis finalizado correctamente.")
print(f"Ventas totales: ${ventas_totales}")
print(f"Producto más vendido: {producto_mas_vendido}")
