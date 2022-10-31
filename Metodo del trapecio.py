#FUNCION DEL METODO DEL TRAPECIO
import numpy as np
import matplotlib.pyplot as plt

def integracion_trapecio(x, y):
  I = []                        #Integral
  if len(y) == len(x):
    n = len(x) - 1              #Cantidad de subintervalos
    a = x[0]                    #Limite de integracion inferior
    b = x[n]                    #Limite de integracion superior
    yn = y[n]                   #Funcion evaluada en la ultima posicion
    sumy = sum(y) - yn - y[0]   #Sumatoria de la formala del metodo del trapecio multiple
    I = round((b - a)*(y[0] + 2*sumy + yn)/(2*n), 6)      #Formula del metodo del trapecio de aplicaciones multiples
  else:
    print("'x' y 'y' deben ser del mismo tamaño")         #Mensaje de alerta

  return(I)

#DATOS DE ENTRADA
a = 0                               #Limite de integracion inferior del problema
b = 0.8                             #Limite de integracion superior del problema
n = 10                              #Numero de subintervalos

#DATOS DE ENTRADA FUNCION
x = np.linspace(a, b, n + 1)        #Generamos los puntos en x. Vector x
y = 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5        #Funcion del problema

#DATOS DE ENTRADA NUMERICOS
#x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#y = [5, 5.5, 5.7, 5.9, 6.3, 6.5, 6.9, 8, 9, 12]

#SOLUCION
print(integracion_trapecio(x, y))
def funcion(x):
  f= 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5
  return f

yn = funcion(x)
plt.plot(x, yn)  # frafica la funcion (establece taaño plano, traza la grafica)
plt.grid(True)
plt.axhline(0, color="#ff0000")  # establece las lineas de origen en x y el color
plt.axvline(0, color="#ff0000")  # establece las lineas de origen en y y el color
plt.title("Metodo trapecio")
plt.ylabel("Eje X")
plt.xlabel("Eje y")
plt.show()