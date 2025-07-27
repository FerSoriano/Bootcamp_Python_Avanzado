"""
El algoritmo de Dijkstra encuentra el camino
mas corto desde un nodo fuente a todos los
otros nodos en un grafo ponderado con pesos de aristas
no negativos

Inicializacion:
Distancia del nodo fuente a el mismo como 0.
Marca la distancia de los demas nodos como no visitados.
Inicializa una cola de prioridad con el nodo fuente, donde
se guardaran los nodos con menor distancia conocidos.

Proceso:
Mientras haya nodos no visitados, extrae el nodo con la distancia mas corta
y actualiza las distancias hacia sus vecinos si encuentra un camino mas corto.
Marca el nodo como visitado.

Repeticion:
Se repite el proceso hasta que todos los nodos han sido visitados.
"""


