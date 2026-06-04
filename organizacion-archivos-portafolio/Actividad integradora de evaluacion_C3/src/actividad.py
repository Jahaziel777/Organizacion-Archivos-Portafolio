import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
df = pd.read_csv("ventas_tecnologia.csv")

# Calcular ingresos
df["ingresos"] = df["cantidad"] * df["precio_unitario"]

# =========================
# REPORTES TABULARES
# =========================

print("VENTAS POR PRODUCTO")
ventas_producto = df.groupby("producto")["cantidad"].sum()
print(ventas_producto)

print("\nVENTAS POR MES")
ventas_mes = df.groupby("mes")["cantidad"].sum()
print(ventas_mes)

print("\nINGRESOS POR PRODUCTO")
ingresos_producto = df.groupby("producto")["ingresos"].sum()
print(ingresos_producto)

print("\nPRODUCTO MAS VENDIDO")
print(ventas_producto.idxmax())

# =========================
# GRAFICA DE BARRAS
# =========================

ventas_producto.plot(kind='bar')
plt.title("Ventas por Producto")
plt.xlabel("Producto")
plt.ylabel("Cantidad Vendida")
plt.show()

# =========================
# GRAFICA DE LINEAS
# =========================

ventas_mes.plot(kind='line', marker='o')
plt.title("Ventas Mensuales")
plt.xlabel("Mes")
plt.ylabel("Cantidad Vendida")
plt.show()

# =========================
# GRAFICA CIRCULAR
# =========================

ventas_producto.plot(kind='pie', autopct='%1.1f%%')
plt.title("Porcentaje de Ventas por Producto")
plt.ylabel("")
plt.show()

# =========================
# PARTE III
# =========================

producto_mayor_ingreso = ingresos_producto.idxmax()
producto_menos_vendido = ventas_producto.idxmin()
mes_mas_rentable = df.groupby("mes")["ingresos"].sum().idxmax()
producto_prioritario = ventas_producto.idxmax()

print("\nPARTE III")
print("Producto con mayores ingresos:", producto_mayor_ingreso)
print("Producto menos vendido:", producto_menos_vendido)
print("Mes más rentable:", mes_mas_rentable)
print("Producto prioritario para inventario:", producto_prioritario)

# =========================
# PARTE IV
# =========================

print("\nPARTE IV")

print("\n¿Qué producto es más importante para la empresa?")
print("El producto más importante es Laptop porque genera mayores ingresos para la empresa.")

print("\n¿Qué información es crítica para la toma de decisiones?")
print("La información más importante son las ventas mensuales y los ingresos por producto, ya que ayudan a controlar inventario y estrategias de venta.")

print("\n¿Qué productos deberían promocionarse más?")
print("Los productos con menores ventas como Teclado y Monitor deberían promocionarse más para aumentar la demanda.")

print("\n¿Qué meses representan mejores oportunidades de venta?")
print("Mayo representa una mejor oportunidad de venta porque fue el mes con mayores ingresos.")