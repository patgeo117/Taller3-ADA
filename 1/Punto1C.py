import random
import time
from Punto1B import stooge_sort

# Se genera un arreglo aleatorio de tamaño n
def generar_arreglo(n):
  A = []
  for i in range(n):
    A.append(random.randint(0, 100))
  return A

# Se prueba el algoritmo con diferentes tamaños de entrada
for n in [10, 100, 1000, 10000]:
  # Se genera un arreglo aleatorio de tamaño n
  A = generar_arreglo(n)
  # Se mide el tiempo inicial
  inicio = time.time()
  # Se aplica el algoritmo de ordenamiento
  stooge_sort(A, 0, n - 1)
  # Se mide el tiempo final
  fin = time.time()
  # Se calcula el tiempo transcurrido
  tiempo = fin - inicio
  # Se imprime el resultado
  print(f"El tiempo de ejecución para n = {n} fue de {tiempo} segundos")
