
def stooge_sort(A, i, j):
  # Si el elemento inicial es mayor que el final, se intercambian
  if A[i] > A[j]:
    A[i], A[j] = A[j], A[i]
  # Si hay más de dos elementos en el arreglo, se aplica la recursión
  if i + 1 < j:
    # Se calcula la tercera parte del tamaño del arreglo
    k = (j - i + 1) // 3
    # Se ordenan las primeras dos terceras partes
    stooge_sort(A, i, j - k)
    # Se ordenan las últimas dos terceras partes
    stooge_sort(A, i + k, j)
    # Se ordenan las primeras dos terceras partes de nuevo
    stooge_sort(A, i, j - k)
  # Se devuelve el arreglo ordenado
  return A

A = [7, 0, 111111, 200, 13, 15, -1]
print(stooge_sort(A, 0, len(A) - 1))
