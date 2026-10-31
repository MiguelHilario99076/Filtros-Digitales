# Diseño de Filtros Digitales en Python

## Descripción

Este proyecto implementa diferentes filtros digitales utilizando Python y las bibliotecas NumPy, SciPy y Matplotlib.

## Filtros implementados

- Filtro pasa bajos (IIR Butterworth)
- Filtro pasa altos (IIR Butterworth)
- Filtro pasa bandas (IIR Butterworth)
- Filtro FIR mediante ventana Hamming

## Objetivo

Analizar el comportamiento de filtros digitales aplicados a señales contaminadas con ruido y evaluar su efectividad mediante gráficas de tiempo y respuesta en frecuencia.

## Herramientas utilizadas

- Python 3.12
- NumPy
- SciPy
- Matplotlib
- Visual Studio Code
- GitHub

## Archivos del proyecto

- filtros.py → Código principal
- comparacion_filtros.png → Comparación de señales
- respuesta_frecuencia.png → Respuesta en frecuencia del filtro
- README.md → Documentación del proyecto

## Instalación

pip install numpy scipy matplotlib

## Ejecución

python filtros.py

## Resultados obtenidos

El programa genera:

1. Señal original con ruido.
2. Señal filtrada mediante filtro pasa bajos.
3. Señal filtrada mediante filtro pasa altos.
4. Señal filtrada mediante filtro pasa bandas.
5. Señal filtrada mediante filtro FIR.
6. Respuesta en frecuencia del filtro pasa bajos.

## Conclusiones

Los filtros digitales permiten eliminar ruido y seleccionar componentes específicas de frecuencia. Los filtros Butterworth mostraron una adecuada atenuación de las frecuencias no deseadas, mientras que el filtro FIR proporcionó una respuesta estable y lineal en fase.

## Autor

Miguel Angel Hilario Lopez