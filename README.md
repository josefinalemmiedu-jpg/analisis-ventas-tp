# Análisis de Ventas de una Pequeña Empresa

## Integrante
- Josefina Lemmi

## Escenario elegido
Escenario B: Análisis de ventas de una pequeña empresa.

## Descripción del proyecto
Este proyecto corresponde al Trabajo Práctico de Gestión Colaborativa, Control de Versiones y Organización Empresarial.

El objetivo es analizar un conjunto de datos simulados de ventas comerciales para obtener indicadores básicos que permitan interpretar el desempeño de una pequeña empresa.

## Dataset utilizado
Se utiliza un archivo CSV llamado ventas.csv, ubicado en la carpeta datos/.

El dataset contiene las siguientes columnas:
- fecha
- producto
- cantidad
- precio

## Indicadores calculados
El script permite calcular:
- ventas totales
- producto más vendido
- ventas por mes

Además, genera un gráfico simple con la evolución de las ventas mensuales.

## Estructura del repositorio
El repositorio se organiza de la siguiente manera:

datos/
- ventas.csv

scripts/
- analisis_ventas.py

resultados/
- resumen_ventas.txt
- grafico_ventas.png

README.md  
.gitignore

## Instrucciones de ejecución
Para ejecutar el proyecto en Google Colab, se debe ingresar a la carpeta del repositorio y ejecutar:

python scripts/analisis_ventas.py

## Herramientas utilizadas
- Jira
- Git
- GitHub
- Google Colab
- Python
- Pandas
- Matplotlib

## Relación con Jira
El trabajo fue organizado mediante un tablero de Jira con las siguientes tareas:

- AV-1: Crear estructura inicial del repositorio
- AV-2: Desarrollar script de análisis de ventas
- AV-3: Revisar documentación y realizar Pull Request

Cada commit debe respetar la trazabilidad con Jira, incluyendo el código de la tarea correspondiente.

## Resultado del análisis
El script de análisis de ventas fue ejecutado correctamente en Google Colab.

Resultados obtenidos:
- Ventas totales: $330000
- Producto más vendido: Remera

Los archivos generados se guardaron en la carpeta resultados/.

## Revisión técnica
Se realizó una revisión del proyecto verificando que:
- el script se ejecute correctamente en Google Colab
- las rutas utilizadas sean relativas
- los resultados se guarden en la carpeta resultados/
- no se exponga el token de GitHub en el repositorio
- el README describa el objetivo, la estructura y la forma de ejecución del proyecto
