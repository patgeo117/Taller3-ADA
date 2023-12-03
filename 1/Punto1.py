import random
import time
import numpy as np


def stooge_sort(A, i, j):
    if A[i] > A[j]:
        A[i], A[j] = A[j], A[i]

    if j - i + 1 > 2:
        t = (j - i + 1) // 3
        stooge_sort(A, i, j - t)
        stooge_sort(A, i + t, j)
        stooge_sort(A, i, j - t)

    return A


# def generar_arreglo():
#     # Crear un arreglo de prueba
#     A = np.array([1,2,3])
#
#     # Llamar a stooge_sort con los índices iniciales y finales
#     result = stooge_sort(A, 0, len(A) - 1)
#
#     return result
#
#
# print(generar_arreglo())


def generar_arreglo(n):
    return [random.randint(0, 100) for _ in range(n)]


# Medir el tiempo de ejecución de un algoritmo
def medir_tiempo_ejecucion(algoritmo, A, i, j):
    inicio = time.time()
    algoritmo(A, i, j)
    fin = time.time()
    return fin - inicio


def main():
    for n in [10, 100, 1000, 2000]:
        A = generar_arreglo(n)
        tiempo = medir_tiempo_ejecucion(stooge_sort, A, 0, len(A) - 1)
        print(f"El tiempo de ejecución para n = {n} fue de {tiempo} segundos")


if __name__ == "__main__":
    main()
