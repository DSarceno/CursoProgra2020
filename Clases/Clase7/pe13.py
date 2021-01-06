#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# @Author: Diego Sarceno
# Date: 10.11.2020
#
#
#

'''Este programa toma 100 numeros el archivo, los suma y toma los primeros
10 digitos'''

file = open('pe13num.txt','r')
data = [line.split() for line in file]

# se suman todos los numeros
sum = 0
for num in data:
    sum += int(num[0])

print(str(sum)[0:10])
