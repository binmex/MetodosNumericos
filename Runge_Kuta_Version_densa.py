import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy import *
#from math import *
from tabulate import tabulate

#metodo de Runge - Kutta de primer orden

def RK1(xi, yi, xf, h):
  n = (xf - xi)/h                                     #cantidad de intervalos
  x = np.linspace(xi, xf, int(n+1))                   #valores de x
  yf=[]                                               #aproximacion de la integral de f'x
  fi = []                                             #derivada f'x
  k1v = []                                            #vector de k1
  yf.append(yi)
  er = []
  er.append("--")
  k1v.append("--")

  for i in range (int(n)):
    k1 = f1(x[i], yf[i])
    yf.append(yf[i] + (k1)*h)
    er.append(abs((yf[i+1] - yf[i])*100/yf[i]))
    k1v.append(k1)

  return (x, yf, k1v, er)

#-------------------------------------------------------------------------------
#metodo de Runge - Kutta de segundo orden

def RK2(xi, yi, xf, h):
  n = (xf - xi)/h                                     #cantidad de intervalos
  x = np.linspace(xi, xf, int(n+1))                   #valores de x
  yf=[]                                               #aproximacion de la integral de f'x
  fi = []                                             #derivada f'x
  k1v = []                                            #vector de k1
  k2v = []                                            #vector de k2
  yf.append(yi)
  er = []
  er.append("--")
  k1v.append("--")
  k2v.append("--")
  #a2 = 1/2                                            #Valor a2 equivalente al Metodo Heun
  #a2 = 1                                             #Valor a2 equivalente al Metodo del punto medio
  a2 = 2/3                                           #Valor a2 equivalente al Metodo de Ralston
  a1 = 1 - a2
  p1 = 1/(2*a2)
  q11 = 1/(2*a2)

  for i in range (int(n)):
    k1 = f1(x[i], yf[i])
    k2 = f1(x[i] + p1*h, yf[i] + q11*k1*h)
    yf.append(yf[i] + (a1*k1 + a2*k2)*h)
    er.append(abs((yf[i+1] - yf[i])*100/yf[i]))
    k1v.append(k1)
    k2v.append(k2)

  return (x, yf, k1v, k2v, er)

#-------------------------------------------------------------------------------
#metodo de Runge - Kutta de cuarto orden

def RK4(xi, yi, xf, h):
  n = (xf - xi)/h                                     #cantidad de intervalos
  x = np.linspace(xi, xf, int(n+1))                   #valores de x
  yf=[]                                               #aproximacion de la integral de f'x
  fi = []                                             #derivada f'x
  k1v = []                                            #vector de k1
  k2v = []                                            #vector de k2
  k3v = []                                            #vector de k3
  k4v = []                                            #vector de k4
  yf.append(yi)
  er = []
  er.append("--")
  k1v.append("--")
  k2v.append("--")
  k3v.append("--")
  k4v.append("--")

  for i in range (int(n)):
    k1 = f1(x[i], yf[i])
    k2 = f1(x[i] + (1/2)*h, yf[i] + (1/2)*k1*h)
    k3 = f1(x[i] + (1/2)*h, yf[i] + (1/2)*k2*h)
    k4 = f1(x[i] + h, yf[i] + k3*h)
    yf.append(yf[i] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)*h)
    er.append(abs((yf[i+1] - yf[i])*100/yf[i]))
    k1v.append(k1)
    k2v.append(k2)
    k3v.append(k3)
    k4v.append(k4)

  return (x, yf, k1v, k2v, k3v, k4v, er)


#===============================================================
#Solucion del ejericio
#===============================================================

#Funcion ecuacion diferencial de primer orden f(x,y)
def f1(x, y):
  dvy1 = -2*x + y*x
  return (dvy1)

def f11(x, y):
  dvy1 = -2 + (-2*x + y*x)*x + y
  return (dvy1)

def f12(x, y):
  dvy1 = -2 + (-2*x + y*x)*x + y
  return (dvy1)

#Solucion analitica
def y(x):
  fx = np.exp((2/3)*x**3 + 0.9996)
  return (fx)

#============================================================
#Valores Iniciales
#============================================================

xi = 1                                #Valor inicial de 'x'
yi = -3                               #Valor inicial de 'y'

#Limite superior de integracion
xf = 2                                #Valor final de 'x'

#Tamaño de Paso o incremento
h1 = 0.1                              #Tamaño de paso 1

#=======================================================
#Llamada de funcion
#=======================================================

#Runge - Kutta de 1er orden
x1_RK1, yf1_RK1, k11_RK1, e1_RK1 = RK1(xi, yi, xf, h1)

#Runge - Kutta de 2do orden
x1_RK2, yf1_RK2, k11_RK2, k12_RK2, e1_RK2 = RK2(xi, yi, xf, h1)

#Runge - Kutta de 4to orden
x1, yf1, k11, k12, k13, k14, e1 = RK4(xi, yi, xf, h1)

#=======================================================
#Tabla de datos
#=======================================================

#Runge-Kutta de 1er orden

print("RUNGE - KUTTA 1er orden")
print(" ")

#Tabla 1
n1 = len(x1)
tabla1 = []                         #tabla de datos
#Llenar la tabla de datos
for i in range(n1):
  tabla1.append([x1_RK1[i], yf1_RK1[i], k11_RK1[i], e1_RK1[i]])

print("tabla de datos 1")
print(" ")
print(tabulate(tabla1, headers=['x', 'y', 'k1', 'er(%)']))
print(" ")
print(" ")

#------------------------------------------------------------------------------
#Runge-Kutta de 2do orden
print(" ")
print(" ")
print("RUNGE - KUTTA 2do orden")
print(" ")

#Tabla 1
n1 = len(x1)
tabla1 = []                         #tabla de datos
#Llenar la tabla de datos
for i in range(n1):
  tabla1.append([x1_RK2[i], yf1_RK2[i], k11_RK2[i], k12_RK2[i], e1_RK2[i]])

print("tabla de datos 1")
print(" ")
print(tabulate(tabla1, headers=['x', 'y', 'k1', 'k2', 'er(%)']))
print(" ")
print(" ")

#------------------------------------------------------------------------------
#Runge-Kutta de 4to orden
print(" ")
print(" ")
print("RUNGE - KUTTA 4to orden")
print(" ")

#Tabla 1
n1 = len(x1)
tabla1 = []                         #tabla de datos
#Llenar la tabla de datos
for i in range(n1):
  tabla1.append([x1[i], yf1[i], k11[i], k12[i], k13[i], k14[i], e1[i]])

print("tabla de datos 1")
print(" ")
print(tabulate(tabla1, headers=['x', 'y', 'k1', 'k2', 'k3', 'k4', 'er(%)']))
print(" ")
print(" ")

#======================================================================
#Solucion Analitica
#======================================================================


#usamos el procedimiento de:
#https://relopezbriega.github.io/blog/2016/01/10/ecuaciones-diferenciales-con-python/
# Resolviendo ecuación diferencial
# defino las incognitas
xs = sympy.Symbol('x')
ys = sympy.Function('y')
e = sympy.Symbol('e')

# expreso la ecuacion
fs = -2*xs + ys(xs)*xs
sympy.Eq(ys(xs).diff(xs), fs)

# Condición inicial
ics = {ys(xi): yi}

# Resolviendo la ecuación
edo_sol = sympy.dsolve(ys(xs).diff(xs) - fs)
edo_sol

#imprimimos la solucion, para copiar la expresion y usarla mas adelante
print(edo_sol)

#Reemplazamos los valores de la condición inicial en nuestra ecuación.

C_eq = sympy.Eq(edo_sol.lhs.subs(xs, xi).subs(ics), edo_sol.rhs.subs(xs, xi))
C_eq

sympy.solve(C_eq)

#Definimos la funcion con la solución analitica
def yanalitic(x, C1):
  ysolv=C1*exp(x**2/2) + 2
  return (ysolv)

#intervalo de evaluacion de la solución analitica
h4 = h1
n4 = (xf - xi)/h4                                       #cantidad de intervalos
x4 = np.linspace(xi, xf, int(n4+1))                     #valores de x
#yf4 = yanalitic(x4, 2)
#x4 = np.array([1, 2])
yf4 = []
for i in range(len(x4)):
  yf4.append(yanalitic(x4[i], -5*np.exp(-1/2)))

#Calculo del error de la aproximacion

yf4abs = yf4[len(yf4) - 1]

er11 = abs((yf1_RK1[len(yf1_RK1) - 1] - yf4abs)/yf4abs)*100
er21 = abs((yf1_RK2[len(yf1_RK2) - 1] - yf4abs)/yf4abs)*100
er31 = abs((yf1[len(yf1) - 1] - yf4abs)/yf4abs)*100

print(er11, er21, er31)

#------------------------------------------------------------------------------
#Runge-Kutta de 2do, 3er y 4to orden
plt.figure(figsize=(15, 12))
plt.plot(x1_RK1, yf1_RK1, '-r', label = "RK 1er orden h = " + str(h1))
plt.plot(x1_RK2, yf1_RK2, '-g', label = "RK 2do orden h = " + str(h1))
plt.plot(x1, yf1, '-b', label = "RK 4to orden h = " + str(h1))
plt.plot(x4, yf4, 'y', label = "solucion analitica = " + str(h4))
#plt.axis([0, 6, 0, 20])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Grafica de la funcion y = f(x)")
plt.legend()
plt.grid()
plt.show()