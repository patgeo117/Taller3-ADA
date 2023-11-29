import random
import time

# Función para generar un arreglo aleatorio de tamaño n
def generar_arreglo(n):
  A = []
  for i in range(n):
    A.append(random.randint(0, 100))
  return A

# Función para implementar el algoritmo QuickSort
def quicksort(A, i, j):
  # Si el arreglo tiene un solo elemento, ya está ordenado
  if i >= j:
    return
  # Se elige el último elemento como pivote
  pivote = A[j]
  # Se inicializa el índice de partición
  k = i
  # Se recorre el arreglo desde el inicio hasta el penúltimo elemento
  for l in range(i, j):
    # Si el elemento actual es menor o igual que el pivote, se intercambia con el elemento en el índice de partición
    if A[l] <= pivote:
      A[l], A[k] = A[k], A[l]
      # Se incrementa el índice de partición
      k += 1
  # Se coloca el pivote en el índice de partición
  A[k], A[j] = A[j], A[k]
  # Se ordena recursivamente la sublista izquierda y la sublista derecha
  quicksort(A, i, k - 1)
  quicksort(A, k + 1, j)

# Función para implementar el algoritmo Insertion-Sort
def insertion_sort(A, n):
  # Se recorre el arreglo desde el segundo elemento hasta el último
  for i in range(1, n):
    # Se guarda el elemento actual como clave
    clave = A[i]
    # Se inicializa el índice del elemento anterior
    j = i - 1
    # Se compara la clave con los elementos anteriores y se mueven los mayores a la derecha
    while j >= 0 and A[j] > clave:
      A[j + 1] = A[j]
      j -= 1
    # Se inserta la clave en su posición correcta
    A[j + 1] = clave

# Función para implementar el algoritmo Merge-Sort
def merge_sort(A, i, j):
  # Si el arreglo tiene un solo elemento, ya está ordenado
  if i >= j:
    return
  # Se calcula el punto medio del arreglo
  m = (i + j) // 2
  # Se ordena recursivamente la sublista izquierda y la sublista derecha
  merge_sort(A, i, m)
  merge_sort(A, m + 1, j)
  # Se mezclan las sublistas ordenadas
  merge(A, i, m, j)

# Función auxiliar para mezclar dos sublistas ordenadas
def merge(A, i, m, j):
  # Se crea una lista vacía para almacenar el resultado
  B = []
  # Se inicializan los índices de las sublistas
  k = i
  l = m + 1
  # Se comparan los elementos de las sublistas y se agregan al resultado en orden
  while k <= m and l <= j:
    if A[k] <= A[l]:
      B.append(A[k])
      k += 1
    else:
      B.append(A[l])
      l += 1
  # Se agregan los elementos restantes de la sublista izquierda, si hay
  while k <= m:
    B.append(A[k])
    k += 1
  # Se agregan los elementos restantes de la sublista derecha, si hay
  while l <= j:
    B.append(A[l])
    l += 1
  # Se copia el resultado en el arreglo original
  for k in range(i, j + 1):
    A[k] = B[k - i]

n = 100
A = generar_arreglo(n)
inicio = time.time()
quicksort(A, 0, n - 1)
fin = time.time()
tiempo = fin - inicio
print(f"El tiempo de ejecución para QuickSort con n = {n} fue de {tiempo} segundos")

print(A)