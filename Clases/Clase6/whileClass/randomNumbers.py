import random

'''Generador de un archivo de numeros aleatorios con incertezas.
Formato del archivo creado: (canitdad de datos: 1000<n<10000)
dato1(0.1<x<1000)   inc1(0<dx<1)    dato2   inc2    dato3   inc3'''

file = open('datos.tsv','w')
for i in range(0,random.randint(1000,10000)):
    file.write(str(random.uniform(0.1,random.randint(1,1000))) + '\t' + str(random.random()) + '\t' + str(random.uniform(0.1,random.randint(1,1000))) + '\t' + str(random.random()) + '\t' + str(random.uniform(0.1,random.randint(1,1000))) + '\t' + str(random.random()) + '\n')

file.close()
