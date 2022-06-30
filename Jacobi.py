import numpy as np

def jacobi(A, b, x0, tol, n):
    D = np.diag(np.diag(A))
    LU = A-D
    x = x0
    err = 100
    for i in range(n):
        D_inv= np.linalg.inv(D)
        xtemp = x
        x = np.dot(D_inv,np.dot(-LU,x))+np.dot(D_inv,b)
        print("iteracion", i+1, ":x = ",x, "Err = ",err)
        err = np.linalg.norm(x-xtemp)
        if err < tol:
            return x
    return x
#sistema a resolver

filas = int(input("ingrese el numero de filas: "))
columnas = int(input("ingrese el numero de columnas"))
matriz =[]
matrizInd = []
matrizSol = []
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor = float(input("Fila {}, Columna {} : ".format(i+1, j+1)))
        matriz[i].append(valor)
print()
for fila in matriz:
    print("[",end=" ")
    for elemento in fila:
        print("{:8.2f}".format(elemento), end=" ")
    print("]")
A= matriz

print("\n================================Ingreso del Vector Independiente================================")
#ingreso de datos para el vector independiente
for ind in range(filas):
    dato = float(input("vector independiente  fila{}".format(ind+1)))
    matrizInd.append(dato)
b = matrizInd
print("\n================================Ingreso del Vector solucion propuesto================================")
#dSol = float(input("ingrese la solucion: "))
for ind in range(filas):
    datoSol = float(input("vector solucion X{}".format(ind+1)))
    matrizSol.append(datoSol)
x0 = matrizSol #vector solucion
print("\n=====================================================================================================")
tol = float(input("ingrese la tolerancia: "))
n = int(input("ingrese el numero de iteraciones maximas: ")) #numero iteraciones
x = jacobi(A,b,x0,tol,n)


