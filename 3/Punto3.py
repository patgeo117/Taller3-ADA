import numpy as np
import time

# Función para generar un arreglo aleatorio de tamaño n con NumPy
def generar_arreglo(n):
    return np.random.randint(5, 10001, size=n)

# Función para implementar el algoritmo QuickSort con NumPy
def quicksort(A):
    if len(A) <= 1:
        return A
    pivote = A[-1]
    menores = A[A < pivote]
    iguales = A[A == pivote]
    mayores = A[A > pivote]
    return np.concatenate((quicksort(menores), iguales, quicksort(mayores)))

# Función para implementar el algoritmo Insertion-Sort con NumPy
def insertion_sort(A):
    for i in range(1, len(A)):
        clave = A[i]
        j = i - 1
        while j >= 0 and A[j] > clave:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = clave
    return A

# Función para implementar el algoritmo Merge-Sort con NumPy
def merge_sort(A):
    if len(A) <= 1:
        return A
    m = len(A) // 2
    izquierda = merge_sort(A[:m])
    derecha = merge_sort(A[m:])
    return merge(izquierda, derecha)

# Función auxiliar para mezclar dos sublistas ordenadas con NumPy
def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

n = 10000
A = generar_arreglo(n)

# Mide el tiempo de ejecución para QuickSort con NumPy
inicio = time.time()
quicksort_resultado = quicksort(A.copy())
tiempo_quicksort = time.time() - inicio
print("Tiempo de ejecución para QuickSort:", str(tiempo_quicksort), "segundos")

# Mide el tiempo de ejecución para Insertion-Sort con NumPy
inicio = time.time()
insertion_sort_resultado = insertion_sort(A.copy())
tiempo_insertion_sort = time.time() - inicio
print("Tiempo de ejecucion para Insertion Sort:", str(tiempo_insertion_sort), "segundos")

# Mide el tiempo de ejecución para Merge-Sort con NumPy
inicio = time.time()
merge_sort_resultado = merge_sort(A.copy())
tiempo_merge_sort = time.time() - inicio
print("Tiempo de ejecucion para Marge Sort:", str(tiempo_merge_sort), "segundos")
