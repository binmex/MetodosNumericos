import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

def function(x):
    y = x ** 3 + 2 * x ** 2 + 10 * x - 20
    return y


print("==============================\nMETODO DE BISECCIÓN\n==============================\n")
xi = float(input('Introduce el valor de xi '))
xu = float(input('Introduce el valor de xu '))
# error = float((input('Introduce el error ')))
raiz = []
biseccion_table = []  # tabla de datos del metodo de biseccion
err = 100
i = 1
raiz.append(0)
# si deseamos reducir el margende error solo cambiamos el condicional del while
while err > 1.0:
    xr = (xi + xu) / 2.0
    if function(xi) * function(xr) > 0:
        xi = xr
        raiz.append(xr)
    else:
        xu = xr
        raiz.append(xr)
    err = float(abs((raiz[i] - raiz[i - 1]) / raiz[i]) * 100)
    biseccion_table.append([i, raiz[i], err])
    i = i + 1

# ===========================================================
# Tabla
# ===========================================================
# Tabla de de datos
print("========================================\nImprtante los valores en la tabla aproxima el 5 decimal\n========================================")
print(tabulate(biseccion_table, headers=["Iteracion", "xr", "ERR %"]))

print("========================================\nLa raíz exacta es: ", xr,"\n========================================\n")

# ===========================================================
# Grafica
# ===========================================================
a = 0  # donde empieza el eje x
b = 10  # donde termina el eje y
n = 100  # la densidad de puntos para la grafica
xn = np.linspace(a, b, n)  # Se generan los valores de x para construir la grafica
yn = function(xn)
plt.plot(xn, yn)  # frafica la funcion (establece taaño plano, traza la grafica)
plt.grid(True)
plt.axhline(0, color="#ff0000")  # establece las lineas de origen en x y el color
plt.axvline(0, color="#ff0000")  # establece las lineas de origen en y y el color
plt.plot(xr, 0, 'ko', label=("Raiz Biseccion"))  # grafica el punto de corte x,y
plt.title("Metodo Biseccion")
plt.ylabel("Eje X")
plt.xlabel("Eje y")
plt.show()
