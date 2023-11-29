def encontrar_moda(A, i, j):
  # Caso base: si el vector tiene un solo elemento, se devuelve ese elemento y su frecuencia
  if i == j:
    return [A[i]], 1
  # Caso recursivo: se divide el vector en dos mitades y se llama al algoritmo sobre cada una
  else:
    # Se calcula el punto medio del vector
    m = (i + j) // 2
    # Se encuentra la moda de la primera mitad
    moda_izq, frec_izq = encontrar_moda(A, i, m)
    # Se encuentra la moda de la segunda mitad
    moda_der, frec_der = encontrar_moda(A, m + 1, j)
    # Se combina las soluciones de las dos mitades
    # Se crea un diccionario para almacenar las frecuencias de los elementos
    frecuencias = {}
    # Se recorre la moda de la primera mitad y se agrega al diccionario
    for elemento in moda_izq:
      frecuencias[elemento] = frec_izq
    # Se recorre la moda de la segunda mitad y se actualiza el diccionario
    for elemento in moda_der:
      # Si el elemento ya está en el diccionario, se suma su frecuencia
      if elemento in frecuencias:
        frecuencias[elemento] += frec_der
      # Si no, se agrega al diccionario con su frecuencia
      else:
        frecuencias[elemento] = frec_der
    # Se encuentra el máximo valor de frecuencia en el diccionario
    max_frec = max(frecuencias.values())
    # Se crea una lista para almacenar la moda del vector completo
    moda = []
    # Se recorre el diccionario y se agrega a la lista los elementos que tienen la máxima frecuencia
    for elemento, frecuencia in frecuencias.items():
      if frecuencia == max_frec:
        moda.append(elemento)
    # Se devuelve la lista de la moda y la máxima frecuencia
    return moda, max_frec

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(encontrar_moda(A, 0, len(A) - 1))
