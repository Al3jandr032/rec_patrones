#!/usr/bin/python
#-*- coding: utf-8 -*-
from __future__ import division
from PIL import Image
import sys

print "nombre del programa",__name__
if __name__ == '__main__':
	if len(sys.argv) > 1:
		print sys.argv[1]
		imagen = Image.open(sys.argv[1])
		imagen.show()
		print(imagen.format)   # JPEG
		print(imagen.mode)   # Tipo de imagen: RGB, CMYK, L, P, etc.
	else:
		print "Uso image.py <nombreImagen>"
