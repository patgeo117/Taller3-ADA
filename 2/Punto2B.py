import numpy as np

def encontrar_moda(A, i, j):
    # Caso base: si el vector tiene un solo elemento, se devuelve ese elemento y su frecuencia
    if i == j:
        return [A[i]], 1
    else:
        # Se combina el vector en un arreglo de NumPy
        arreglo_np = np.array(A[i:j+1])
        # Usamos la función unique de NumPy para obtener los elementos únicos y sus frecuencias
        elementos, frecuencias = np.unique(arreglo_np, return_counts=True)
        # Encontramos el índice del elemento con la máxima frecuencia
        indice_max_frec = np.argmax(frecuencias)
        # Obtenemos la moda y su frecuencia
        moda = elementos[frecuencias == frecuencias[indice_max_frec]]
        max_frec = frecuencias[indice_max_frec]
        return moda.tolist(), max_frec

A = [1, 2, 3, 3,4, 5, 6, 7, 8, 9, 1]
print(encontrar_moda(A, 0, len(A) - 1))

