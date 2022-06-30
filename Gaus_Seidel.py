import numpy

m = int(input('Valor de m filas:'))  # filas
n = int(input('Valor de n columnas:'))  # columnas
matrix = numpy.zeros((m, n))
comp = numpy.zeros((m))  # comprobacion de los x por eso usamos m
vector = numpy.zeros((n))  # crear vector con dimension n  osea n columnas lo llena de ceros
vectorNuevo = numpy.zeros((m))  # crear vector con dimension n  osea n columnas lo llena de ceros
x = numpy.zeros((m))
for i in range(0, m):
    print('Introduce vector inicial o iteracion 1 ')
    x[(i)] = float(input("Elemento a[" + str(i + 1) + "] "))

error = []
print('Método de Gauss-Seidel')
print('Introduce la matriz de coeficientes y el vector solución')
for r in range(0, m):  # para pedir los coeficietes de la matriz
    for c in range(0, n):
        matrix[(r), (c)] = float(input("Elemento a[" + str(r + 1) + str(c + 1) + "] "))
    vector[(r)] = float(input('b[' + str(r + 1) + ']: '))
tol = 0.001  # error porcentual
itera = 20
k = 0
while k < itera:  # Para detenerme si las iteraciones se pasan a las que le puse
    suma = 0
    k = k + 1
    for r in range(0, m):
        suma = 0
        for c in range(0, n):
            if (c != r):
                suma = suma + matrix[r, c] * x[c]
        x[r] = (vector[r] - suma) / matrix[r, r]
        print("x[" + str(r) + "]: " + str(x[r]))
    del error[:]
    # Comprobación
    for r in range(0, m):
        suma = 0
        for c in range(0, n):
            suma = suma + matrix[r, c] * x[c]

        comp[r] = suma
        dif = abs(comp[r] - vector[r])
        error.append(dif)
        print("Error x[", r, "]=", error[r])
    print("iteraciones :", k + 1)
    if all(i <= tol for i in error) == True:
        break
