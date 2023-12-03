import random
import time
from Punto2B import encontrar_moda


# Función para generar un arreglo aleatorio de tamaño n
def generar_arreglo(n):
  return [random.randint(0, 100) for _ in range(n)]


# Se prueba el algoritmo con diferentes tamaños de entrada
for n in [10, 100, 1000, 10000]:
  # Se genera un arreglo aleatorio de tamaño n
  A = generar_arreglo(n)

  # Se mide el tiempo inicial
  inicio = time.time()

  # Se aplica el algoritmo para encontrar la moda
  moda, frecuencia = encontrar_moda(A, 0, n - 1)

  # Se mide el tiempo final
  fin = time.time()

  # Se calcula el tiempo transcurrido
  tiempo = fin - inicio

  # Se imprime el resultado
  print(f"El tiempo de ejecución para n = {n} fue de {tiempo} segundos")
  print(f"La moda es {moda} y se repite {frecuencia} veces")

