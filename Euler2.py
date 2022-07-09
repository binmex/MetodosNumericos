import math
from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt
euler_table = []  # tabla de datos del metodo de biseccion
def funcionx(x,y):
    ec = x+2*y
    return ec
def solucion(x,y):
    sol = 0.25*math.exp(2*x)-0.5*x-0.25
    return sol
h = float(input("tamaño de paso: "))
s = float(input("hasta que valor?: "))

#cuantos espacios o iteraciones se vana a ahcer
n = (s/h)+1
x = np.zeros(int(n))
y = np.zeros(int(n))
ys = np.zeros(int(n))

# valores de inicio
x[0] = 0
y[0] = 0
print(x[0],y[0])
for i in np.arange(1,int(n)):
    y[i] = y[i-1]+(funcionx(x[i-1],y[i-1]))*h
    x[i] = x[i-1]+h
    ys[i] = solucion(x[i-1], y[i-1])
    euler_table.append([i, x[i], y[i]])
    #print(x[i], y[i])

print(tabulate(euler_table, headers=["Iteracion", "x", "y"]))
plt.scatter(x,y)
plt.plot(x,y)
plt.scatter(x,ys,color="red")
plt.plot(x,ys,color="red")
plt.grid()
plt.show()