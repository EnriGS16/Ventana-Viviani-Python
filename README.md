# Ventana de Viviani - Python

Programa desarrollado en Python para calcular una aproximación del perímetro
de la Ventana de Viviani utilizando una Suma de Riemann.

## Descripción

El programa utiliza un método numérico basado en una Suma de Riemann para
aproximar la longitud de la curva correspondiente a la Ventana de Viviani.

El usuario puede ingresar:

- El radio de la esfera.
- La cantidad de subintervalos utilizados en la aproximación.
- La cantidad de decimales que desea mostrar en el resultado.

## Método utilizado

El cálculo se realiza mediante una suma numérica de los valores del
integrando evaluados en los puntos medios de los subintervalos.

Al aumentar la cantidad de subintervalos, se obtiene una aproximación
más detallada de la longitud de la curva.

## Características

- Validación del radio ingresado.
- Validación de la cantidad de subintervalos.
- Configuración de la cantidad de decimales.
- Uso de Sumas de Riemann.
- Cálculo numérico del perímetro aproximado.

## Tecnología utilizada

- Python
- Biblioteca estándar `math`

## Ejecución

Ejecutar el programa mediante:

```bash
python CodigoCV.py