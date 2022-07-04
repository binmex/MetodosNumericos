import numpy as np
import matplotlib.pyplot as plt

#metodo de euler para la aproximacion de 1er orden de y dado y' = f(x, y)

#Funcion ecuacion diferencial de primer orden f(x,y)
def f1(x, y):
  dvy1 = -2*x + y*x   #para modificar o incluir la funcion de tu problema
  return (dvy1)

#Solucion analitica
def y(x, y):
  fx = 0                          #El problema no tiene solucion analitica
  return (fx)

#Valores iniciales
xi = 1                            #Valor inicial de 'x'
yi = -3                           #Valor inicial de 'y'
xf = 2                            #Valor final de 'x'
h = 0.1                           #Tamaño de paso

n = (xf - xi)/h                                     #Cantidad de pasos o iteraciones de la aproximacion de la funcion
x = np.linspace(xi, xf, int(n+1))
#fx = y(x)                                          #Solucion analitica de la integral de f'x
yf=[]                                               #aproximacion de la integral de f'x
yf.append(yi)
fi = []
fi.append(f1(xi, yi))                               #derivada f'x

for i in range (int(n)):
  fi.append(f1(x[i], yf[i]))
  yf.append(yi + fi[i]*h)                           #Formula del metodo de Euler
  yi = yf[i+1]

plt.plot(x, yf, 'r')                                 #Grafica
print(x,yf)
plt.show()                                           #Mostrar Grafica