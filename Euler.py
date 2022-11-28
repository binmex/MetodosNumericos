import math
from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt
euler_table = []  # tabla de datos del metodo de biseccion1
def funcionx(x,y):
    ec = -y**2
    return ec

s = float(input("hasta que valor quiere ir: "))
h = float(input("ingrese el ancho: "))


#cuantos espacios o iteraciones se vana a hacer
n = (s/h)+1
x = np.zeros(int(n))
y = np.zeros(int(n))
#vector para comprobar la solucion
ys = np.zeros(int(n))

#================================================
# valores de inicio
#================================================
x[0] = 0
y[0] = 1

#euler_table.append([0,0,0])
for i in np.arange(1,int(n)):
    y[i] = y[i-1]+h*(funcionx(x[i-1],y[i-1]))
    x[i] = x[i-1]+h
    euler_table.append([i-1, x[i], y[i]])

print(tabulate(euler_table, headers=["Iteracion", "x", "y"]))
plt.scatter(x,y)
plt.plot(x,y)
plt.title("Metodo Euler")
plt.ylabel("Eje X")
plt.xlabel("Eje y")
plt.grid()
plt.show()