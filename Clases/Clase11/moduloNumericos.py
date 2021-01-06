#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# @Author: Diego Sarceno
# Date: 13.12.2020
#
#
#
# MODULO METODOS NUMÉRICOS
import sympy as sym
import math as m

# METODO: Euler para solucion de ED's con condiciones iniciales
def Euler(xo,xf,yo,n,exp):
    ''' Método de Euler: (y_i+1 = y_i + F(x_i,y_i)*\Delta x)

            Toma una ecuacion diferencial (exp) de la forma
                    y' = F(x,y)         (implementacion con funciones lambda)
            Con condiciones inicilales
                    y(xo) = yo
            Esto se realiza para un intervalo cerrado
                    [xo,xf]
            Con 'n' subintervalos.

        Retorna una lista de la forma:
            [...,[i,x_i,y_i,F(x_i,y_i),y_i+1],...]
    '''

    # Toma las condiciones inciales y crea los subintervalos
    data = []
    x = xo
    y = yo
    Dx = (xf - xo)/n
    # Itera el método de Euler 'n' veces
    for i in range(n):
        line = [str(i + 1),str(x),str(y)]
        slope = exp(x,y)
        ny = y + slope*Dx
        line.append(str(slope))
        line.append(str(ny))
        data.append(line)
        y = ny
        x += Dx
    # devuelve la lista de datos y el valor aproximado de y(xf)
    return data, data[len(data) - 1][4]


# METODO: Newton para encontrar raíces de funciones
def Newton(x,f,fp):
    ''' Método de Newton: (x_i+1 = x_i - f(x)/f'(x))

            Toma una funcion y su derivada (como funciones lambda) y, por la
            naturaleza del método, toma un valor cercano a la raíz
            que se desee calcular.

        Retorna una lista con los valores de cada iteración.
            [x_1,x_2, ..., x_n]

            donde f(x_n) \approx 0
    '''

    # Crea la lista donde se almacenarán los datos
    dx = []

    # Itera el método de Newton
    while round(f(x),5) != 0:
        nx = x - f(x)/fp(x)
        dx.append(nx)
        x = nx
    # Devuelve la lista de datos y el valor apdimado de la raíz
    return dx, dx[len(dx) - 1]


# METODO: De Trapecios para calular el valor de cierta integral
def Trapecio(a,b,n,exp):
    ''' Método de integración del trapecio: (Ver libro Eq: 3.11)

            Toma una función a integrar (como funcion lambda), los extremos del
            intervalo de integración y el número de subintervalos.

        Retorna el valor aproximado de la integral. (type: float)
    '''

    # Crea la 'h' y el término independiente del método
    h = (b - a)/n
    int = 0.5*(exp(b) - exp(a))

    # Itera el método de los trapecios 'n' veces
    for i in range(1,n):
        x = a + i*h
        int += h*exp(x)
    return int


# METODO: Logitud de arco
def lArc(a,b,x,exp):
    ''' Longitud de Arco: (Def clásica de los libros y Wikipedia xd)
                Es necesario tener importado la librería sympy y
                haber inisializado la variable 'x'.

            Toma el intervalo y el número de subintervalos, además de
            la funcion a utilizar.

        Retorna el valor de la longitud de arco. (type: float)
    '''

    # Encuentra la derivada de la función
    fp = sym.diff(exp,x)

    # La integra en el intervalo dado respecto a la definicion de L.A.
    s = sym.integrate(sym.sqrt(1 + (fp)**2),(x,a,b))
    return s
