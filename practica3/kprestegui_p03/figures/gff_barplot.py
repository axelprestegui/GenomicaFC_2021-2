#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

with open('barplot_data.txt', 'r', encoding='utf-8') as data:
    categorias = []
    frecuencias = []
    for linea in data:
        datos = linea.strip().split()
        print(datos)
        categorias.append(datos[0])
        frecuencias.append(datos[1])
    categorias = [ '\n'.join(wrap(l, 11)) for l in categorias]

    y_pos = np.arange(len(categorias))

    # Gráfico de barras
    plt.bar(y_pos, frecuencias)

    # Nombres en el eje-x
    plt.xticks(y_pos, categorias, rotation=90)

    # Mostrar la gráfica
    plt.show()