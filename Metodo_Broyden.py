#Metodo de Broyden
from math import cos,sin,pi,exp,sqrt
import numpy as np

#se declaran las 3 funciones
def Fs(x1,x2,x3):
    f1 = 3*x1-cos(x2*x3)-1/2
    f2 = x1**2-81*(x2+0.1)**2+sin(x3)+1.06
    f3 = exp(-x1*x2)+20*x3+(10*pi-3)/3
    return np.matrix([[f1],[f2],[f3]]) #al momento de convertirla en una matriz sera una fila

#hallamos el jacoviano y lo invertimos
def Jinv(x1,x2,x3):
    Ja = np.matrix([[3,x3*sin(x2*x3),x2*sin(x2*x3)],[2*x1,-162*(x2+0.1),cos(x3)],[-x2*exp(-x1*x2),-x1*exp(-x1*x2),20]])
    JI = np.linalg.inv(Ja)
    return JI
#imprimimos archivo de cabecera
print("k \t x1 \t\t x2 \t\t x3 \t\t||x(k)-x(k-1)||")

n = 10
X0 = [0.1,0.1,-0.1]
Tol = 0.000001

#seguir al pie de la letra
a = Jinv(X0[0],X0[1],X0[2])
v = Fs(X0[0],X0[1],X0[2])
s = -a*v
X0 = np.matrix(X0).T+s  #.T es para transponer
k = 2

while k<n:
    w = v
    v = Fs(float(X0[0][0]),float(X0[1][0]),float(X0[2][0]))
    y = v-w
    z = -a*y
    p = float(s.T*a*y)
    a = a+1/p*(s+z)*s.T*a
    s = -a*v
    X0 = X0+s
    mag = sqrt(float(s[0][0])**2+float(s[1][0])**2+float(s[2][0])**2)
    print("{0:1d} \t {1:1.6f} \t {2:1.6f} \t {3:1.6f} \t {4:1.6f}".format(k,float(X0[0][0]),float(X0[1][0]),float(X0[2][0]),mag))
    if mag < Tol:
        print("El procedimiento fue exitoso")
        break
    k += 1

