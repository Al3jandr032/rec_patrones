#!/usr/bin/python
#-*- coding: latin-1 -*-
from __future__ import division
import Image                      # funciones para cargar y manipular imágenes
import numpy as np                # funciones numéricas (arrays, matrices, etc.)
import matplotlib.pyplot as plt   # funciones para representación gráfica
# Esta línea configura matplotlib para que muestre figuras en el cuaderno IPython, en lugar de en una ventana nueva. 
# No hay que usarla en los scripts de Python 
#matplotlib inline
#abre imagen
I = Image.open("lambo.jpg")

#La variable, I, no es una matriz, sino un objeto. Podemos visualizarla y realizar algunas operaciones estándard con ella. Por ejemplo, podemos visualizar la imagen
I.show()

#Obtener información sobre la imagen, en este caso el tamaño, tipo (escala de grises, RGB, etc.), y formato:
print I.size, I.mode, I.format

#Convertirla a otro formato, en este caso a una imagen de escala de grises, que son con las que trabajaremos en este curso:
I1=I.convert('L') # convierte a escala de grises
print I1.mode
