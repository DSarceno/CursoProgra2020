#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# @Author: Diego Sarceno
# Date: 8.12.2020
#
#
#

# abrir el archivo
file = open('ej1data.txt','r')

# leer el archivo
DATA = [line.split() for line in file]

# sumar todos los numeros
suma = 0
for i in range(len(DATA)):
    suma += int(DATA[i][0])

# imprimir los primeros 10 digitos
print(str(suma)[0:10])
