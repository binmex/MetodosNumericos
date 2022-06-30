from numpy import sign
from numpy.lib.scimath import sqrt
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

muller_table = []  # tabla de datos del metodo de biseccion

# --------Se ingresa la funcion------
def funcion(x):
    f = x**3+2*x**2+10*x-20
    return f


# ===================================================================
# --------------------------Ingreso de datos------------------------
# ===================================================================
print('============================================================')
print('------------------------Metodo Muller-----------------------')
print('============================================================\n')
x0 = float(input('ingrese el X0: '))
x1 = float(input('Ingrese el X1: '))
x2 = float(input('ingrese el X2: '))
tol = float(input('Ingrese la tolerancia: '))

#ejecucion de la logica
# def muller(x0, x1, x2, tol):
error = 1
x3 = 0
i = 1
while error > tol:
    c = funcion(x2)
    b = ((x0 - x2) ** 2 * ((funcion(x1)) - (funcion(x2))) - (x1 - x2) ** 2 * ((funcion(x0)) - (funcion(x2)))) / (
            (x0 - x2) * (x1 - x2) * (x0 - x1))
    a = ((x1 - x2) * (funcion(x0) - funcion(x2)) - (x0 - x2) * (funcion(x1) - funcion(x2))) / (
            (x0 - x2) * (x1 - x2) * (x0 - x1))
    x3 = x2 - (2 * c) / (b + sign(b) * sqrt(b ** 2 - 4 * a * c))
    error = abs(x3 - x2) #obtencion de valor absoluto
    x0 = x1
    x1 = x2
    x2 = x3
    muller_table.append([i,x3,error]) #ingreso de datos a la tabla
    #si el resultado es imaginario y desean saber el valor en cada iteracion descomentar la linea a continuacion
    #print('iteracion ',i,'valor de x3: ',x3)
    i += 1
#return x3
r = x3

print("========================================\nImprtante los valores en la tabla aproxima el 5 decimal\n========================================")
print(tabulate(muller_table, headers=["Iteracion", "X3", "ERR %"]))

print('--------------------La raiz es: ',r,'--------------------')


# ========================================================================================
# ----------------------------------------Graficar----------------------------------------
# ========================================================================================
a = -5  # donde empieza el eje x
b = 5  # donde termina el eje x
n = 50  # la densidad de puntos para la grafica
xn = np.linspace(a, b, n)  # Se generan los valores de x para construir la grafica
yn = funcion(xn)
plt.plot(xn, yn)  # frafica la funcion (establece taaño plano, traza la grafica)
plt.grid(True)
plt.axhline(0, color="#ff0000")  # establece las lineas de origen en x y el color
plt.axvline(0, color="#ff0000")  # establece las lineas de origen en y y el color
plt.plot(r, 0, 'ko', label=("Raiz Biseccion"))  # grafica el punto de corte x,y
plt.title("Metodo Miuler")
plt.ylabel("Eje X")
plt.xlabel("Eje y")
plt.show()
