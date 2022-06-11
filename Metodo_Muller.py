from numpy import sign
from numpy.lib.scimath import sqrt
from tabulate import tabulate

# metodo para hallar raices complejas siuuuuuuuuuuuuuuuuuu
muller_table = []  # tabla de datos del metodo de biseccion
raiz=[]  #donde se va a ir guardadnod las raices

# Se ingresa la funcion
def funcion(x):
    f = x ** 2 + 2 * x + 5
    return f


def muller(x0, x1, x2, tol):
    error = 0.001
    x3 = 0
    i=0
    while error > tol:
        c = funcion(x2)
        b = ((x0 - x2) ** 2 * ((funcion(x1)) - (funcion(x2))) - (x1 - x2) ** 2 * ((funcion(x0)) - (funcion(x2)))) / (
                    (x0 - x2) * (x1 - x2) * (x0 - x1))
        a = ((x1 - x2) * (funcion(x0) - funcion(x2)) - (x0 - x2) * (funcion(x1) - funcion(x2))) / (
                    (x0 - x2) * (x1 - x2) * (x0 - x1))
        x3 = x2 - (2 * c) / (b + sign(b) * sqrt(b ** 2 - 4 * a * c))
        error = abs(x3 - x2)
        x0 = x1
        x1 = x2
        x2 = x3
        raiz.append(x3)
        muller_table.append(raiz[i])
        i +=1
    return x3


# ===================================================================
# --------------------------Ingreso de datos------------------------
# ===================================================================
print('============================================================')
print('------------------------Metodo Muller-----------------------')
print('============================================================\n')
X0 = float(input('ingrese el X0: '))
X1 = float(input('Ingrese el X1: '))
X2 = float(input('ingrese el X2: '))
Tol = float(input('Ingrese la tolerancia: '))
print("========================================\nImprtante los valores en la tabla aproxima el 5 decimal\n========================================")
print('La raiz es: ', muller(X0, X1, X2, Tol))

