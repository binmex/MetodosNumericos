import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
#Newton - Raphson
def NewtonRaphson(x1, es, imax):
    x = x1  # aproximaciones de la raiz
    xv = []  # vector que guarda las aproximaciones de la raiz
    ea = 2 * es  # error absoluto
    eav = []  # vector que guarda el error absoluto
    i = 0  # numero de iteraciones
    niter = []  # v0ector del numero de iteraciones
    fxv = []  # vector de la funcion f(x)
    Newton_table = []  # tabla de datos del metodo newton - raphson

    Newton_table.append([i, x, f1(x), f(x), "--", "--"])  #colocamos la primera fila de datos en la 1 iteracion
    xv.append(x)

    while ea > es and i <= imax:
        x = x - f(x) / f1(x)  # formula de newton - raphson
        xv.append(x)
        fxv.append(f1(x))
        i += 1
        niter.append(i)

        if x != 0:
            ea = abs((xv[i] - xv[i - 1]))
            er = abs((xv[i] - xv[i - 1]) / xv[i]) * 100  # error relativo
            eav.append(ea)
        Newton_table.append([i, x, f1(x), f(x), ea, er])
    print('====================================================\n'
          'el valor exacto de la raiz es: ',x,
          '\n====================================================')
    # Tabla de de datos
    print("Metodo Newton-Raphson")
    print(tabulate(Newton_table, headers=["Iteracion", "x", "f'(x)", "|f(x)| < er", "e abs = Xac - Xat < er", "er (%) => (Xac-Xat/Xac)*100"]))

    return (x, f(x))
#=========================================================

#Valores para graficar la funcion
a = 0          #Valor inicial del rango de x para graficar
b = 10           #Valor final del rango de x para graficar
n = 50           #Cantidad de puntos


#Parametros para controlar las aproximaciones
#emax = 10**-3
emax = float(input('ingrese el margen de error que desea'))
itermax = float(input('Ingrese el numero de iteraciones maximas'))
x1 = float(input('ingrese el valor inicial'))


#f(x) formula original
x = np.linspace(a, b, n)     #Se generan los valores de x para construir la grafica
def f(xs):
  f_x = xs**3-xs-1  #Valor de la funcion para cada x
  return (f_x)

#f'(x) - Derivada de f(x)
def f1(xs):
  f1_x = 3*xs**2-1
  return (f1_x)


fx = f(x)

xr, yr = NewtonRaphson(x1, emax, itermax)

print("Grafica de la funcion")
plt.figure(figsize=(6, 4))
plt.plot(x, fx, label=("fx"))
plt.plot(x, np.zeros(len(x)), 'k:', label=("0"))
plt.axvline(0,color="#000000")
plt.plot(xr, yr, 'ko', label=("Raiz Newton"))  #grafica el punto de corte
plt.xlabel("x axis")            #Etiqueta de eje
plt.ylabel("y axis")            #Etiqueta de eje
plt.title("Grafica Newton Rapson") #Titulo del grafico
plt.legend()                    #Leyendas
plt.grid(True)
plt.show()                      #Mostrar grafico


