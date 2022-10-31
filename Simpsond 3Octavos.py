import numpy as np

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


def integracion_sim13(x, y):              #Definicion de la funcion
  I = []                                  #Valor acumulado de la integral

  if len(y) == len(x):                    #Comparar tamaño de los vectores de la variable 'x' y 'y'
    n = len(x) - 1                        #cantidad de subintervalos

    if n%2 == 0:                          #Verificacion del numero de subintervalos par
      a = x[0]                            #Limite de integracion inferior
      b = x[n]                            #Limite de integracion superior
      sumy1 = 0                           #Sumatoria del valor de la funcion en las posiciones impares
      sumy2 = 0                           #Sumatoria del valor de la funcion en las posiciones pares

      for i in range(1, n):               #ciclo para llevar a cabo las sumatorias

        if i%2 != 0:                      #Condicional para posiciones impares
          sumy1 += y[i]                   #Sumatoria de impares

        else:
          sumy2 += y[i]                   #Sumatoria de pares

      I = round((b - a)*(y[0] + 4*sumy1 + 2*sumy2 + y[n])/(3*n), 6) #Formula de la regla de simpson 1/3 multiple

    else:
      print("+")

  else:
    print("'x' y 'y' deben ser del mismo tamaño")

  return(I)


def integracion_sim38(x, y):
  I = 0                   #Valor acumulado de la integral

  if len(y) == len(x):    #Comparacion de la longitud de los vectores 'x' y 'y'
    n = len(x) - 1        #cantidad de segmentos
    nres = n%3            #segmentos residuales de la regla 3/8
    n38 = int((n - nres)/3)    #cantidad de tramos para la integracion por la regla 3/8
    I38 = 0               #Integral regla 3/8
    I13 = 0               #Integral regla 1/3
    I1  = 0               #Integral trapecio
    I   = 0               #Integral de la funcion

    for i in range(n38):  #ciclo regla de simpson 3/8
      a = x[3*i]          #limite de integracion inferior del tramo de la regla 3/8
      b = x[3*(i+1)]      #limite de integracion superior del tramo de la regla 3/8
      y0 = y[3*i]         #valor de la funcion en el punto 0 del subintervalo
      y1 = y[3*i + 1]     #valor de la funcion en el punto 1 del subintervalo
      y2 = y[3*i + 2]     #valor de la funcion en el punto 2 del subintervalo
      y3 = y[3*i + 3]     #valor de la funcion en el punto 3 del subintervalo
      I38 += (b - a)*(y0 + 3*y1 + 3*y2 + y3)/8  #formula de la regla de simpson

    if nres == 2:         #condicional para la regla de simpson 1/3
      x2 = [x[n-2], x[n-1], x[n]]     #vector x del tramo sobrante para la regla 1/3
      y2 = [y[n-2], y[n-1], y[n]]     #vector y del tramo sobrante para la regla 1/3
      I13 = integracion_sim13(x2, y2) #integral de la regla 1/3 del tramo sobrante

    elif nres == 1:       #condicional para la regla del trapecio
      x1 = [x[n-1], x[n]]             #vector x del tramo sobrante para la regla del trapecio
      y1 = [y[n-1], y[n]]             #vector y del tramo sobrante para la regla del trapecio
      I1 = integracion_trapecio(x1, y1) #integral de la regla del trapecio del tramo sobrante

    I = round(I38 + I13 + I1, 6)      #Total de la integral numerica

  else:
    print("'x' y 'y' deben ser del mismo tamaño")

  return(I)

#============================================================================0

#DATOS DE ENTRADA
a = 0                       #Limite de integracion inferior del problema
b = 0.8                     #Limite de integracion superior del problema
n = 10                      #Cantidad de subintervalos

#DATOS DE ENTRADA FUNCION
x = np.linspace(a, b, n + 1)  #Vertor de las posiciones en 'x'
y = 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5  #Vector de la funcion evaluada en 'x'

#DATOS DE ENTRADA NUMERICOS
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y = [5, 5.5, 5.7, 5.9, 6.3, 6.5, 6.9, 8, 9, 12, 15]

print(integracion_sim38(x, y))           #solucion numerica de la integral