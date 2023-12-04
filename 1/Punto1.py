import random
import time

def stooge_sort(arr):
    # Algoritmo de ordenamiento Stooge Sort
   if len(arr) <= 1:
       return arr

   if arr[0] > arr[-1]:
       arr[0], arr[-1] = arr[-1], arr[0]

   if len(arr) > 2:
       t = len(arr) // 3
       arr[:t] = stooge_sort(arr[:t])
       arr[-t:] = stooge_sort(arr[-t:])
       arr[:t] = stooge_sort(arr[:t])

   return arr

def test_sort_algorithm(sort_function, array_size, function_name):
    # Genera un arreglo de numeros aleatorios
   arr = [random.randint(1, 1000) for _ in range(array_size)]

   try:
       # Calcula el tiempo de ejecución del algoritmo
       start_time = time.time()
       sorted_arr = sort_function(arr)
       end_time = time.time()
       elapsed_time = end_time - start_time

       # print del tiempo de ejecución
       print("Tamaño del arreglo:", array_size)
       print("Tiempo de ejecución: {:.6f} segundos".format(elapsed_time))

       # print del arreglo original
       print("Arreglo original:", arr)

       # print del arreglo ordenado
       print("Arreglo ordenado:", sorted_arr)

       # chequea que el arreglo esté ordenado correctamente
       assert sorted_arr == sorted(arr), "El arreglo no está ordenado correctamente"

   except Exception as e:
       # excepción en caso de que el algoritmo tarde demasiado en ejecutarse
       print(f"Error: {e}")
       print(f"El tiempo de ejecución para el arreglo de tamaño {array_size} fue demasiado largo.")



# Ejemplos de uso
test_sort_algorithm(sorted, 10, "sorted")
test_sort_algorithm(sorted, 100, "sorted")
test_sort_algorithm(sorted, 1000, "sorted")
test_sort_algorithm(sorted, 10000, "sorted")