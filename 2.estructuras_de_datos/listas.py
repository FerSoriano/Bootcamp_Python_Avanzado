
import copy


"""
Las listas se pasan por referencia no por copia.
si asignamos una lista a una nueva variable y despues modificamos un
elemento, entonces esta afectara a la nueva lista
Ejemplo:
"""
lista1 = [1, 2, 3]
lista2 = lista1
print(lista2)  # [1, 2, 3]
lista2[0] = 9
print(lista1)  # [9, 2, 3]

"""
Para evitar esto, debemos usar alguna de las sig opciones:
    - .copy()
    - slicing: lsita1[:]
    - list(lista1)
"""
lista1 = [1, 2, 3]
lista2 = lista1.copy()
print(lista2)  # [1, 2, 3]
lista2[0] = 9
print(lista1)  # [1, 2, 3]

"""
Tambien se puede usar list comprehension
para copiar los valores de una lista a otra
"""
lista1 = [1, 2, 3]
lista2 = [x for x in lista1]
print(lista2)  # [1, 2, 3]
lista2[0] = 9
print(lista1)  # [1, 2, 3]

"""
Precaución: copias profundas
Si tu lista contiene elementos mutables (por ejemplo, otras listas),
entonces necesitas una copia profunda:
"""
lista1 = [[1, 2], [3, 4]]
lista2 = copy.deepcopy(lista1)
lista2[0][1] = 10
print(lista1)  # [[1, 2], [3, 4]]
