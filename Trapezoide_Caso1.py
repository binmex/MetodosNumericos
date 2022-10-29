import matplotlib.pyplot as plt
import numpy as np

#entradas

#---->Funcion:
fx = lambda x: 2+3*x

# Intervalo de integracion
a = 0
b = 5

#segmentos o trapecios a formar
#entre mas trapecios mas precicion
trapecios = 1

h = (b-a)/trapecios

#metodo Trapezoidal
muestras = trapecios+1
areaTotal = 0

xi = a

#no hace la de 1
for i in range(0,trapecios,1):
    areaTrapecio = h*(fx(xi)+fx(xi+h))/2
    areaTotal = areaTotal+areaTrapecio
    #avance al siguiente trapecio
    xi += h
#crear una distribucion de puntos equidistantes
xi = np.linspace(a,b,muestras)
#evaluamos cada punto xi en la funcion original
fi= fx(xi)

#salidas
print('cantidad de trapecios: ', trapecios)
print('El resultado de la integral es: ', areaTotal)
#grafica puntos de muestra incluyendo los
plt.plot(xi,fi,'bo')
#dibujamos lineas para dividir los trapecios
for i in range(0,muestras,1):
    plt.axvline(xi[i],color='w')
    #rellenamos los trapecios/llenar entre
    plt.fill_between(xi,0,fi,color='red')
    plt.show()

