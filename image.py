#!/usr/bin/python
#-*- coding: latin-1 -*-
from __future__ import division
from PIL import Image
imagen = Image.open("ipn.jpg")
imagen.show()
print(imagen.format)   # JPEG
print(imagen.mode)   # Tipo de imagen: RGB, CMYK, L, P, etc.
