file = open('textoaleatorio.txt','r')

'''
linea1 = file.readline()
print(file.readline())

linea2 = file.readline()
print(linea2)

lastLine = file.readline()
print(lastLine)
'''

#DATA = file.readlines()
#print(DATA)

DATA = [line.split() for line in file]
print(DATA)
