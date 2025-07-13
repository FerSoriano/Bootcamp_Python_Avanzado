
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista Original: ", lista1)

"""
Usar list comprehension para FILTRAR
"""
numeros_pares = [x for x in lista1 if x % 2 == 0]
print("Numeros Pares: ", numeros_pares)

"""
Usar list comprehension para MODIFICAR
"""
numeros_al_cuadrado = [x * x for x in lista1]
print("Numeros al Cuadrado: ", numeros_al_cuadrado)

"""
Usar list comprehension para MODIFICAR por CONDICION
"""
numeros_pares_al_cuadrado = [x * x if x % 2 == 0 else x for x in lista1]
print("Numeros Pares al Cuadrado: ", numeros_pares_al_cuadrado)
