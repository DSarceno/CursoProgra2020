


from datetime import datetime
import math as m

# crear la funcion de la ED

def F(x,y):
    return x*y

def solution(x):
    return m.exp((x**2 - 1)/2)


def Euler(xo,xf,yo,n):
    data = []
    x = xo
    y = yo
    Dx = (xf - xo)/n
    for i in range(n):
        line = [str(i + 1),str(x),str(y)]
        slope = F(x,y)
        ny = y + slope*Dx
        line.append(str(slope))
        line.append(str(ny))
        data.append(line)
        y = ny
        x += Dx
    return data

def tablaTex(data):
    '''type(data) == list'''
    now = datetime.now()
    name = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second) + '.tex'
    file = open(name,'w')
    file.write('\\hline \n')
    file.write('\\hline \n')
    file.write('$i$ & $x_i$ & $y_i$ & $F(x_i ,y_i)$ & $y_{i+1}$ \\\\ \n')
    file.write('\\hline \n')
    file.write('\\hline \n')
    for line in data:
        nline = '$ {index} $ & $ {xi} $ & $ {yi} $ & $ {F} $ & $ {nyi} $ \\\\ \n'
        file.write(nline.format(index = line[0], xi = line[1], yi = line[2], F = line[3], nyi = line[4]))
    file.write('\\hline \n')
    file.close()
    return data



def pData(data):
    for x in data:
        print(x)
    return

def ePorc(data, xf):
    error = (1 - float(data[len(data) - 1][4])/solution(xf)) *100
    return error

# solicitar el numero de intervalos, las condiciones iniciales y el punto final del intervalos
xo = float(input('Inicio del Intervalo: '))
yo = float(input('Condicion inicial: '))
xf = float(input('Fin del Intervalo: '))
n = int(input('Numero de Subintervalos: '))


pData(tablaTex(Euler(xo,xf,yo,n)))
print(ePorc(Euler(xo,xf,yo,n),xf))
