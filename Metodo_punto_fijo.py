import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
#funcion original
def originalFunction(x):
    f_x=np.cos(x)-3*x
    return f_x
#funcion despejada
def clearanceFunction(x):
    g_x=np.cos(x)/3
    return g_x

print('====================================================\n'
      'metodo punto fijo '
      '\n====================================================\n')

puntoFijo_table = []  # tabla de datos del metodo de biseccion
root = []
x = float(input('ingrese el valor inicial'))
errorF = float(input('ingrese el error maximo que desea'))
err = 100
i = 1;
root.append(x)

while abs(err) > errorF:
    xs = clearanceFunction(x)
    root.append(xs)
    err = ((root[i]-root[i-1])/root[i])*100
    puntoFijo_table.append([i+1,x,xs, abs(originalFunction(x)),abs(err)])
    x = xs
    i +=1
#============================================================
#Tabla
#============================================================
print(tabulate(puntoFijo_table, headers=["Iteracion", "x", "g(x) => raiz","f(x)", "err %"]))
print('el valor exacto de la raiz es: ',x)

# ===========================================================
# Grafica
# ===========================================================
a = -2  # donde empieza el eje x
b = 2  # donde termina el eje y
n = 100  # la densidad de puntos para la grafica
xn = np.linspace(a, b, n)  # Se generan los valores de x para construir la grafica
yn = originalFunction(xn)
plt.plot(xn, yn)  # frafica la funcion (establece taaño plano, traza la grafica)
plt.grid(True)
plt.axhline(0, color="#ff0000")  # establece las lineas de origen en x y el color
plt.axvline(0, color="#ff0000")  # establece las lineas de origen en y y el color
plt.plot(x, 0, 'ko', label=("Raiz Punto fijo"))  # grafica el punto de corte x,y
plt.title("Metodo Punto fijo")
plt.ylabel("Eje X")
plt.xlabel("Eje y")
plt.show()