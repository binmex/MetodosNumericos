
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

runge_kutta_table = []  # tabla de datos del metodo de biseccion
def runge_kutta_system(f, g, x0, y0, a, b, h):
    t = np.arange(a, b + h, h)
    n = len(t)
    x = np.zeros(n)
    y = np.zeros(n)
    x[0] = x0
    y[0] = y0

    for i in range(n - 1):
        k1 = h * f(x[i], y[i], t[i])
        l1 = h * g(x[i], y[i], t[i])
        k2 = h * f(x[i] + k1 / 2, y[i] + l1 / 2, t[i] + h / 2)
        l2 = h * g(x[i] + k1 / 2, y[i] + l1 / 2, t[i] + h / 2)
        k3 = h * f(x[i] + k2 / 2, y[i] + l2 / 2, t[i] + h / 2)
        l3 = h * g(x[i] + k2 / 2, y[i] + l2 / 2, t[i] + h / 2)
        k4 = h * f(x[i] + k3, y[i] + l3, t[i] + h)
        l4 = h * g(x[i] + k3, y[i] + l3, t[i] + h)
        x[i + 1] = x[i] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + 2 * k4)
        y[i + 1] = y[i] + (1 / 6) * (l1 + 2 * l2 + 2 * l3 + 2 * l4)
        runge_kutta_table.append([k1,l1,k2,l2,k3,l3,k4,l4,x[i + 1],y[i + 1]])
        print(tabulate(runge_kutta_table, headers=["K1", "l1", "k2", "l2", "k3", "l3", "k4", "l4", "x", "y"]))
        plt.plot(t, x, t, y)
        plt.show()

print("========================================\nImprtante los valores en la tabla aproxima el 5 decimal\n========================================")
print(tabulate(runge_kutta_table, headers=["K1", "l1", "k2","l2","k3","l3","k4","l4","x","y"]))
#==========================================
#ingreso de datos
#==========================================

f = lambda x,y,t: -0.1*x
g = lambda x,y,t: -0.1*x-0.2*y
x0 = 5000
y0 = 0
a = 0
b = 20
h = 0.5

runge_kutta_system(f,g,x0,y0,a,b,h)