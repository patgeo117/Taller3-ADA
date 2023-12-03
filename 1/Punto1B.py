
import numpy as np

def stooge_sort(A):
    n = len(A)

    # Si el elemento inicial es mayor que el final, se intercambian
    if A[0] > A[-1]:
        A[0], A[-1] = A[-1], A[0]

    # Si hay más de dos elementos en el arreglo, se aplica la recursión
    if n > 2:
        # Se calcula la tercera parte del tamaño del arreglo
        k = n // 3
        # Se ordenan las primeras dos terceras partes
        stooge_sort(A[:n - k])
        # Se ordenan las últimas dos terceras partes
        stooge_sort(A[k:])
        # Se ordenan las primeras dos terceras partes de nuevo
        stooge_sort(A[:n - k])

    return A

A = np.array([7, 0, 111111, 200, 13, 15, -1])
print(stooge_sort(A))