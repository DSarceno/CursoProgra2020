#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# @Author: Diego Sarceno
# Date: 13.12.2020
#
#
#
# PRUEBA DE MÓDULOS


import sympy as sym
import moduloNumericos as mn
import data

'''
x = sym.symbols('x')
f = input('Ingrese funcion a integrar: ')
a = int(input('Inicio del intervalo: '))
b = int(input('Fin del intervalo: '))
s = mn.lArc(a,b,x,f)
print(float(s))
'''

f = lambda x,y: x*y

sol = mn.Euler(1,2,1,1000,f)
print(sol[1])

table = data.tableTex(sol[0],'prueba')
base = data.dataBase(sol[0],'pruebaDatos','tsv')
print(table, base)
