#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# @Author: Diego Sarceno
# Date: 10.11.2020
#
#
#

'''Este programa lee un archivo de números aleatorios y calculará
la multiplicación con incerteza y escribirá todo en un nuevo archivo'''

import math as m

# Abrimos el archivo de dats .tsv
file = open('datos.tsv','r')

# Se leen las líneas del archivo
data = [line.split() for line in file]
file.close()

# Navegamos por 'data' realizando las multiplicaciones y lo almacenamos en 'q'
Q = []
for block in data:
    q = float(block[0]) * float(block[2]) * float(block[4])
    dq = q*m.sqrt((float(block[1]) / float(block[0])) + (float(block[3]) / float(block[2])) + (float(block[5]) / float(block[4])))
    Q.append([str(q),str(dq)])


# Escribimos el archivo con los valores y su incerteza
file = open('incertProd.tsv','w')

# Empezamos a escribir los datos obtenidos
for q in Q:
    dato = '{n1}' + '\t' + '{n2}' + '\n'
    file.write(dato.format(n1 = q[0], n2 = q[1]))

file.close()
