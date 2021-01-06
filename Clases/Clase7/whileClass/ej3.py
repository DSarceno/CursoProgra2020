#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# @Author: Diego Sarceno
# Date: 8.12.2020
#
#
#

# Leer el archivo y extraer datos
file = open('Q.tsv','r')
DATA = [line.split() for line in file]
file.close()


# arbir el .tex y escribir el preambulo
file = open('QTable.tex','w')

file.write('\\documentclass[11pt, spanish, letterpage]{article} \n')
file.write('\\usepackage[spanish, es-noshorthands]{babel} \n')
file.write('\\usepackage[utf8]{inputenc} \n')
file.write('\\usepackage{graphicx} \n')
file.write('\\usepackage{float} \n')
file.write('\\title{Tabla de Datos} \n')
file.write('\\author{Yo} \n')
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

# crear la tabla y escrirla
for i in range(16):
    line = '$ {q} $ & $ {dq} $ \\\\ \n'
    file.write(line.format(q = str(DATA[i][0]), dq = str(DATA[i][1])))

file.write('\\hline \n')
file.write('\\hline \n')
file.write('\\end{tabular} \n')
file.write('\\caption{Datos} \n')
file.write('\\end{table} \n')
file.write('\\end{document}')
# cerramos el archivo
file.close()

# SUBPROCESS
import subprocess
subprocess.call(['pdflatex','QTable.tex'])
subprocess.call(['rm', 'QTable.aux'])
subprocess.call(['rm', 'QTable.log'])
subprocess.call(['rm', 'QTable.out'])
subprocess.call(['evince', 'QTable.pdf'])


'''
subprocess.run('pdflatex "tabla.tex"', shell = True)
subprocess.run('del "tabla.aux"', shell=True)
subprocess.run('del "tabla.log"', shell=True)
subprocess.run('del "tabla.out"', shell=True)
'''
