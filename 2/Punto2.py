#librerias
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

def encontrar_moda(arr):
    # Ordenar el vector utilizando QuickSort
    arr_sorted = quicksort(arr)

    # Inicializar variables para la moda
    moda = []
    max_frecuencia = 1
    frecuencia_actual = 1

    # Encontrar la moda recorriendo el vector ordenado
    for i in range(1, len(arr_sorted)):
        if arr_sorted[i] == arr_sorted[i - 1]:
            frecuencia_actual += 1
        else:
            frecuencia_actual = 1

        if frecuencia_actual > max_frecuencia:
            moda = [arr_sorted[i]]
            max_frecuencia = frecuencia_actual
        elif frecuencia_actual == max_frecuencia:
            moda.append(arr_sorted[i])

    return moda, max_frecuencia

def generar_arreglo(n):
    return [random.randint(0, 100) for _ in range(n)]

# Ejemplos de uso
vector1 = [1, 2, 2, 3, 4]
vector2 = [1, 2, 2, 3, 3, 5]

def vector3():

    for n in [10, 100, 1000, 2000]:
        arr = generar_arreglo(n)
        print("Vector 3: ", arr)
        print("Vector 3 - La moda es:", encontrar_moda(arr))

print("Vector 1:", vector1)
print("Vector 1 - La moda es:", encontrar_moda(vector1))

print("Vector 2:", vector2)
print("Vector 2 - La moda es:", encontrar_moda(vector2))

vector3()
