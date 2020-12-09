#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# @Author: Diego Sarceno
# Date: 8.12.2020
#
#
#

'''ñakldsasdfasldkfasdnfasdfjadjfñalksjdfñladksfñlcalksdjbfkla
lkajsdflkajbdslkfals'''

from math import sqrt

# abrir y leer el archivo
file = open('datos.tsv', 'r')
DATA = [line.split() for line in file]
file.close()


# calcular q y \delta q
Q = []
for datos in DATA:
    q = float(datos[0]) * float(datos[2]) / float(datos[4])
    dq = q * sqrt((float(datos[1]) / float(datos[0])) + (float(datos[3]) / float(datos[2])) + (float(datos[5]) / float(datos[4])))
    Q.append([q,dq])

#print(Q)

# Escribir el nuevo archivo
file = open('Q.tsv','w')

for datos in Q:
    file.write(str(datos[0]) + '\t' + str(datos[1]) + '\n')

file.close()
