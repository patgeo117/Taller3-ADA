# librerias
import random

# Implementación de QuickSort con Python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)


# Encontrar la moda de un vector utilizando QuickSort
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

# Función para generar un arreglo aleatorio de tamaño n
def generar_arreglo(n):
    return [random.randint(0, 100) for _ in range(n)]


# Ejemplos de uso
vector1 = [1, 2, 2, 3, 4]
vector2 = [1, 2, 2, 3, 3, 5]

# Generar un vector aleatorio de tamaño n y encontrar su moda
def vector():
    for n in [10, 100, 1000, 2000]:
        arr = generar_arreglo(n)
        print(f"Vector de tamaño {n} --> {arr}")
        print("La moda es:", encontrar_moda(arr))


print(f"Vector de tamaño {len(vector1)} --> {vector1}")
print("La moda es:", encontrar_moda(vector1))

print(f"Vector de tamaño {len(vector2)} --> {vector2}")
print("La moda es:", encontrar_moda(vector2))

vector()
