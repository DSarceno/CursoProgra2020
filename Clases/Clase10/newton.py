

# se crean las funciones
def f(x):
    return x**2 - 11*x + 30

def fp(x):
    return 2*x - 11

# iterador para el método de newton
def Newton(x):
    dx = []
    '''
    for i in range(100):
        nx = x - f(x)/fp(x)
        dx.append(nx)
        if round(f(x),5) == 0:
            break
    '''
    while round(f(x),5) != 0:
        nx = x - f(x)/fp(x)
        dx.append(nx)
        x = nx
    return dx

def pData(data):
    for x in data:
        print(x)
    return

pData(Newton(0.5))
