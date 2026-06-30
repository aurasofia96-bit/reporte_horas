# Reporte de Horas Semanales

Programa desarrollado en Python para calcular el total de horas trabajadas por cada empleado durante una semana laboral y clasificar su jornada según las horas registradas.

## Descripción

El programa recorre una lista de trabajadores con las horas laboradas de lunes a viernes, calcula el total semanal mediante una función y determina si el trabajador cumplió la jornada estándar, trabajó horas extras o estuvo por debajo de la jornada establecida.

## Características

- Calcula las horas trabajadas por semana.
- Clasifica la jornada laboral en:
  - Horario Estándar (40 horas)
  - Sobretiempo (más de 40 horas)
  - Inferior (menos de 40 horas)
- Muestra un reporte organizado para cada trabajador.
- Uso de funciones para separar la lógica del programa.

## Tecnologías

- Python 3

## Cómo ejecutar

1. Clona este repositorio o descarga el archivo.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta:

```bash
python reporte_horas.py
```

## Ejemplo de salida

```text
--------------------------------------------------

 Reporte de horas semanales por trabajador

--------------------------------------------------

Nombre del trabajador: David
Total de horas semanales: 42
Clasificación de jornada: Sobretiempo

Nombre del trabajador: Liz
Total de horas semanales: 37
Clasificación de jornada: Inferior

...
```

## Lo que practiqué

En este proyecto utilicé:

- Listas anidadas
- Funciones
- Bucles `for`
- Condicionales (`if`, `elif`, `else`)
- Acumuladores
- Parámetros y valores de retorno
- Impresión de reportes en consola

## Posibles mejoras

- Permitir ingresar trabajadores desde el teclado.
- Leer la información desde un archivo CSV o Excel.
- Calcular el pago de horas extras.
- Mostrar estadísticas generales del equipo.
- Exportar el reporte a un archivo.

## Estado del proyecto

Proyecto finalizado como práctica de Python.
