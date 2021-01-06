#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# @Author: Diego Sarceno
# Date: 13.12.2020
#
#
#
# MODULO ESCRITURA DE ARCHIVOS

# Tabla latex
def tableTex(data,name):
    '''Creador de tablas en latex:

            Toma un conjunto de datos y realiza una tabla en formato latex
            con el nombre ingresado 'name'.

        Toma -> Devuelve
        [...,[...,sublist,...],...] -> name.tex (tabla)
    '''
    # Toma el nombre con su extension y crea el archivo
    name += '.tex'
    file = open(name,'w')

    # Escribe la tabla en formato latex
    for sublist in data:
        line = ''
        for i in range(len(sublist)):
            if (i + 1) == len(sublist):
                line += sublist[i] + ' \\\\ \n'
            else:
                line += sublist[i] + ' & '
        file.write(line)
    file.close()
    return 'Done Bitch!'


# creación de base de datos
def dataBase(data,name,fileType):
    '''Creador de archivos de datos:

            Toma un conjunto de datos y realiza un archivo (.txt, .tsv,
            etc.) con el nombre ingresado 'name'.

        Toma -> Devuelve
        [...,[...,sublist,...],...] -> name.fileType (datos)
    '''

    # Toma el nombre con la extension y crea el archivo
    name += '.' + fileType
    file = open(name,'w')

    # Escribe el archivo de datos
    for sublist in data:
        line = ''
        for i in range(len(sublist)):
            if (i + 1) != len(sublist):
                line += sublist[i] + ' \t '
            elif (i + 1) == len(sublist):
                line += sublist[i] + ' \n'
        file.write(line)
    file.close()
    return 'Done again Bitch!!'
