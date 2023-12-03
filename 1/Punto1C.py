import random
import time
from Punto1B import stooge_sort

def generar_arreglo(n):
    return [random.randint(0, 100) for _ in range(n)]

def medir_tiempo_ejecucion(algoritmo, A):
    inicio = time.time()
    algoritmo(A)
    fin = time.time()
    return fin - inicio

# Se prueba el algoritmo con diferentes tamaños de entrada
for n in [10, 100, 1000, 10000]:
    # Se genera un arreglo aleatorio de tamaño n
    A = generar_arreglo(n)

    # Se mide el tiempo de ejecución
    tiempo = medir_tiempo_ejecucion(stooge_sort, A)

    # Se imprime el resultado
    print(f"El tiempo de ejecución para n = {n} fue de {tiempo} segundos")
