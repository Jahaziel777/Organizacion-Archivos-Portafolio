# Sistema de Análisis y Visualización de Ventas con Python

## Descripción

Sistema desarrollado para analizar información de ventas de una tienda de tecnología mediante el procesamiento de datos almacenados en un archivo CSV. Permite generar reportes tabulares, visualizar información mediante gráficas y obtener indicadores relevantes para apoyar la toma de decisiones comerciales.

## Objetivo

Desarrollar una aplicación en Python capaz de procesar información de ventas, generar reportes estadísticos y representar visualmente los resultados para identificar tendencias, productos con mayor demanda, productos más rentables y oportunidades de mejora en las estrategias de venta.

## Tecnologías Utilizadas

* Python 3
* Pandas (Procesamiento y análisis de datos)
* Matplotlib (Visualización gráfica de información)
* CSV (Almacenamiento de datos de ventas)
* Visual Studio Code (Entorno de desarrollo)

## Estructura del Proyecto

* ventas_tecnologia.csv: Archivo que contiene la información de ventas.
* actividad.py: Programa principal encargado de procesar los datos.
* Reporte PDF: Documento con capturas, análisis e interpretación de resultados.
* README.md: Documentación general del proyecto.

## Formatos de Archivo Utilizados

### CSV: Almacenamiento de Datos

El sistema utiliza un archivo CSV para almacenar la información de ventas. Se eligió este formato por las siguientes ventajas:

* *Simplicidad:* Permite almacenar datos mediante filas y columnas de forma organizada.
* *Compatibilidad:* Puede abrirse en Excel, Google Sheets y ser procesado por Python.
* *Facilidad de procesamiento:* Pandas permite leer y analizar los datos de manera eficiente.
* *Portabilidad:* Es un formato ligero y fácil de compartir.

### Reportes Tabulares

Los reportes tabulares permiten organizar la información de forma estructurada para facilitar su análisis.

* *Organización clara:* Los datos se presentan en filas y columnas.
* *Facilidad de consulta:* Permiten localizar información específica rápidamente.
* *Ordenamiento y filtrado:* Facilitan el análisis detallado de los datos.
* *Apoyo a la toma de decisiones:* Ayudan a identificar tendencias y comportamientos de venta.

## Funcionamiento del Sistema

1. Cargar el archivo ventas_tecnologia.csv.
2. Leer los datos mediante la librería pandas.
3. Calcular los ingresos generados por cada producto.
4. Generar reportes tabulares de ventas e ingresos.
5. Identificar los productos más vendidos y más rentables.
6. Generar gráficas utilizando matplotlib.
7. Mostrar resultados para apoyar la toma de decisiones.

## Reportes Generados

El sistema genera los siguientes reportes:

* Ventas totales por producto.
* Ventas totales por mes.
* Ingresos generados por producto.
* Producto más vendido.
* Producto con mayores ingresos.
* Producto menos vendido.
* Mes más rentable.
* Producto prioritario para inventario.

## Gráficas Generadas

### Gráfica de Barras

Representa las ventas totales por producto, permitiendo comparar fácilmente el desempeño de cada artículo.

### Gráfica de Líneas

Muestra la evolución de las ventas a lo largo de los meses analizados.

### Gráfica Circular

Representa el porcentaje de participación de cada producto dentro de las ventas totales.

## Interpretación de Resultados

El análisis permite identificar los productos con mayor demanda, aquellos que generan mayores ingresos y los periodos más favorables para las ventas. Esta información puede utilizarse para optimizar inventarios, desarrollar promociones y mejorar la rentabilidad de la empresa.

## Capturas del Sistema Funcionando

Se incluyen evidencias del funcionamiento del programa mostrando los reportes tabulares, las gráficas generadas y los resultados obtenidos durante el análisis.

## Documentación

La documentación incluye la explicación del análisis realizado, la interpretación de resultados, las conclusiones obtenidas y las evidencias gráficas del funcionamiento del sistema.
