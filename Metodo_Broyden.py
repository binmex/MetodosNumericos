#Metodo de Broyden
from math import cos,sin,pi,exp,sqrt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#se declaran las 3 funciones
def Fs(x1,x2):
    f1 = 4*x1**2-20*x1+1/4*x2**2+8
    f2 = 1/2*x1*x2**2+2*x1-5*x2+8
    return np.matrix([[f1],[f2]]) #al momento de convertirla en una matriz sera una fila

#hallamos el jacoviano y lo invertimos
def Jinv(x1,x2):
    Ja = np.matrix([[8*x1-20,1/2*x2],[1/2*x2**2+2,x1*x2-5]])
    JI = np.linalg.inv(Ja)
    return JI

#imprimimos archivo de cabecera
print("k \t x1 \t\t x2 \t\t||x(k)-x(k-1)||")

n = 10
X0 = [0,0]
Tol = 0.1

#seguir al pie de la letra
a = Jinv(X0[0],X0[1])
v = Fs(X0[0],X0[1])
s = -a*v
X0 = np.matrix(X0).T+s  #.T es para transponer
k = 2
#print(v)
#print(float(X0[0][0]))
#print(float(X0[1][0]))
print("=======================")
while k<n:
    w = v
    v = Fs(float(X0[0][0]),float(X0[1][0]))
    #print(v)
    #print('valor de  A:',a)
    y = v-w
    z = -a*y
    p = float(s.T*a*y)
    a = a+1/p*(s+z)*s.T*a
    s = -a*v
    X0 = X0+s
    mag = sqrt(float(s[0][0])**2+float(s[1][0])**2)
    print("{0:1d} \t {1:1.6f} \t {2:1.6f} \t {3:1.6f}".format(k,float(X0[0][0]),float(X0[1][0]),mag))
    if mag < Tol:
        print("El procedimiento fue exitoso")
        break
    k += 1
#===========================================================
#-------------------------Graficar--------------------------

def funGraf(x,y):
    f_x = 4*x**2-20*x+1/4*y**2+8
    return f_x
def funGraf2(x,y):
    f_x = 1/2*x*y**2+2*x-5*y+8
    return f_x
fig = plt.figure()
ax = Axes3D(fig)
a = -10
b = 10
c = 50
x = np.linspace(a,b,c)
y = np.linspace(a,b,c)
#graficar con superficio
X , Y = np.meshgrid(x,y)
Z,W = np.meshgrid(x,y)

#ax.plot(x, y, funGraf(x,y))
a#x.plot(x, y, funGraf2(x,y))
ax.plot_surface(X,Y,funGraf(X,Y))
ax.plot_surface(X,Y,funGraf2(Z,W))

#ax.axvline(0,color="#ff0000")
#ax.axhline(0,color="#ff0000")
ax.grid(True)
ax.scatter(float(X0[0][0]),float(X0[0][0]))
print('el punto donde se graico es: ',float(X0[0][0]))
plt.show()