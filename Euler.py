import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

euler_table = []  # tabla de datos del metodo de biseccion
#metodo de euler para la aproximacion de 1er orden de y dado y' = f(x, y)

#Funcion ecuacion diferencial de primer orden f(x,y)
def f1(x, y):
  dvy1 = x-y   #para modificar o incluir la funcion de tu problema
  return (dvy1)

#Solucion analitica
def y(x, y):
  fx = 1.10364                          #El problema no tiene solucion analitica
  return (fx)

#Valores iniciales
xi = 0                            #Valor inicial de 'x'
yi = 2                           #Valor inicial de 'y'
xf = 1                            #Valor final de 'x'
h = 0.000001                           #Tamaño de paso

n = (xf - xi)/h                                     #Cantidad de pasos o iteraciones de la aproximacion de la funcion
x = np.linspace(xi, xf, int(n+1))
#fx = y(x)                                          #Solucion analitica de la integral de f'x
yf=[]                                               #aproximacion de la integral de f'x
yf.append(yi)
fi = []
fi.append(f1(xi, yi))                               #derivada f'x
ys = []
ys.append(y(xi, yi))

for i in range (int(n)):
  fi.append(f1(x[i], yf[i]))
  #ys.append(y(x[i],yf[i]))
  yf.append(yi + fi[i]*h)                           #Formula del metodo de Euler
  yi = yf[i+1]
  euler_table.append([i,x[i],yf[i]])

plt.plot(x, yf, 'b')                                 #Grafica
#plt.scatter(x,yf,color="blue")
plt.grid(True)
#plt.plot(x,ys,color="red")
print(tabulate(euler_table, headers=["Iteracion", "x", "y"]))
#print(x,yf)
plt.show()                                           #Mostrar Grafica