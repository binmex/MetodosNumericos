x0 = 0.00
x1 = 0.00
x2 = 0.00
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
Secante_table = []  # tabla de datos del metodo newton - raphson

def function(x):
    y = x**2-3*x-4  #formula a evaluar
    return y

print("METODO DE RECTA SECANTE")
x0 = float(input('Introduce el valor de x0 '))
x1 = float(input('Introduce el valor de x1 '))
errorF = float((input('Introduce el error ')))

raiz = []
itera = []
raiz.insert(0, 0)
itera.insert(0, 0)

i = 0
error = 1

while abs(error) > errorF:
    itera.append(i)
    x2 = x1 - (function(x1) * (x1 - x0)) / (function(x1) - function(x0))
    raiz.append(x2)
    x0 = x1
    x1 = x2
    i = i + 1
    error = (raiz[i] - raiz[i - 1])
    Secante_table.append([i,x2,abs(error),function(raiz[i]),raiz[i] - (function(raiz[i]) * (raiz[i] - raiz[i-1])) / (function(raiz[i]) - function(raiz[i-1])) ])
# Tabla de de datos
print(" ")
print("Metodo Newton-Raphson")
print(tabulate(Secante_table, headers=["Iteracion", "x", "error => xact -Xant < err", "f(raiz) < err", "g(x) ~ raiz"]))
print("La raíz exacta encontrada es: ", x2)

a = 0
b=10
n=100
xn = np.linspace(a, b, n)     #Se generan los valores de x para construir la grafica
yn = function(xn)
plt.plot(xn, yn)
plt.grid(True)
plt.axhline(0,color="#ff0000")
plt.axvline(0,color="#ff0000")
plt.plot(x2,0, 'ko', label=("Raiz secante"))  #grafica el punto de corte x,y
plt.ylabel("Valor de la raiz")
plt.xlabel("Numero de iteracion")
plt.show()