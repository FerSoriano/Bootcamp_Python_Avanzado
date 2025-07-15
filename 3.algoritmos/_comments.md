# Tipos de Algorimos en este Modulo

---

- QuickSort
  - Ordenamiento rapido
- Djkstra
  - Camino mas corto
- BST (Binary Search Tree)
  - Arbol de busqueda binaria
- K-means
  - Agrupamiento de similares

---

# Complejidad Temporal

El numero de operaciones crece a medida que aumenta el tamaño de la entrada.

### Ejemplo Big O: O(n)

```python
def busqueda_lineal(arr, goal):
    for i in range(len(arr)):
        if arr[i] == goal:
            return True
    return False
```

> A medida que incrementan los elementos, crece el tiempo.

### Ejemplo Big O: O(log n)

```python
def busqueda_binaria(arr, goal):
    left = 0
    rigth = 0

    while  left <= rigth:
        mid = (left + rigth) // 2
        if arr[mid] == goal:
            return mid
        elif arr[mid] < goal:
            left = mid + 1
        else:
            rigth = mid - 1

    return -1
```

> Un algoritmo es O(log n) cuando el tamaño del problema se reduce a la mitad en cada iteración. Esto es típico en algoritmos como la búsqueda binaria, donde en cada paso se descarta la mitad de los datos.
