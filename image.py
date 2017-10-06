#!/usr/bin/python
#-*- coding: utf-8 -*-
from __future__ import division
from PIL import Image
import sys

print "nombre del programa",__name__
if __name__ == '__main__':
	if len(sys.argv) > 1:
		print sys.argv[1]
		try:
			imagen = Image.open(sys.argv[1])
			print "tipo dato Image.open :",type(imagen)
			if imagen is not None:
				if imagen.mode != "RGB":
					imagen.show()
					print(imagen.format)   # JPEG
					print(imagen.mode)
					print(imagen.size) 
					pix = imagen.load()
					print "RGB : ",pix[0,0] #Get the RGBA Value of the a pixel of an image
				else:
					print "Solo trabajo con imagenes en rgb" 
		except Exception as e:
			print "Error al abrir la imagen"
		
		  # Tipo de imagen: RGB, CMYK, L, P, etc.
	else:
		print "Uso image.py <nombreImagen>"
