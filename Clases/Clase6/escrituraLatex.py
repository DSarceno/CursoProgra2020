#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# @Author: Diego Sarceno
# Date: 10.11.2020
#
#
#

'''Este programa utiliza los datos encontrados en el programa
-lecturaArchivos.py- y se escribe ciertas lineas de datos en una tabla'''

# Se leen los datos del archivo 'incertProd'
file1 = open('incertProd.tsv','r')
data = [line.split() for line in file1]
file1.close()

file = open('tabla.tex','w')

file.write('\\documentclass[11pt, spanish, letterpage]{article} \n')
file.write('\\usepackage[spanish, es-noshorthands]{babel} \n')
file.write('\\usepackage[utf8]{inputenc} \n')
file.write('\\usepackage{graphicx} \n')
file.write('\\usepackage{float} \n')
file.write('\\title{Tabla de Datos} \n')
file.write('\\author{Yo}')
file.write('\\date{\\today} \n')
file.write('\\begin{document} \n')
file.write('\\maketitle \n')

# Ahora creamos el entorno de la Tabla
file.write('\\begin{table}[H] \n')
file.write('\\centering \n')
file.write('\\begin{tabular}{||c|c||} \n')
file.write('\\hline \n')
file.write('\\hline \n')
file.write('$q$ & $\\delta q$ \\\\ \n')
file.write('\\hline \n')
file.write('\\hline \n')


# escritura de la Tabla
for i in range(10):
    q = '$' + '{n1}' + '$ & $' + '{n2}' + '$ \\\\ \n'
    file.write(q.format(n1 = data[i][0], n2 = data[i][1]))



file.write('\\hline \n')
file.write('\\hline \n')
file.write('\\end{tabular} \n')
file.write('\\caption{Datos} \n')
file.write('\\end{table} \n')
file.write('\\end{document}')

# Utilizamos el modulo subprocess para correrlo desde la terminal
import subprocess
subprocess.run('pdflatex "tabla.tex"', shell=True)
subprocess.run('del "tabla.aux"', shell=True)
subprocess.run('del "tabla.log"', shell=True)
subprocess.run('del "tabla.out"', shell=True)
# subprocess.run('evince "tabla.pdf"', shell=True)
