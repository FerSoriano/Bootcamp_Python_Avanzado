"""
Generator Funcions:
son tipos especiales de funciones que permiten
crear itreadores usando una funcion

La palabra clave yield convierte una función normal en un generator function.
Cuando se llama a esta función, no se ejecuta su cuerpo inmediatamente.
En lugar de eso, retorna un generator object, que puede ir produciendo valores
uno a uno cada vez que se llama a next().

Cada vez que se alcanza un yield, la ejecución se pausa y guarda todo el estado
interno de la función (variables locales, el contador del bucle, etc.)
Cuando se vuelve a llamar a next(), la ejecución se reanuda justo después
del yield anterior, como si nada hubiera pasado.
"""

nums = [1, 2, 3, 4, 5]


def sequence_generator(sequence):
    for item in sequence:
        yield item
        # return item # Si usamos return no podremos iterar la funcion.


for num in sequence_generator(nums):
    print(num)

"""
Con este tipo de generadores, no es necesario calcular todo en memoria,
sino que lo vamos usando cuando lo vayamos necesitando
Ejemplo:
"""
print("\n---- Pairs Generator ----")


def pairs_gen(max):
    for i in range(0, max, 2):
        yield i


generator = pairs_gen(100)
"""A pesar de que le pasamos el Max de 100, no usamos todos de golpe"""
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

"""
Podemos recorrerlo con un bucle si queremos recorrer hasta el Max
Lo interesante, es que continuara desde el ulitmo elemento que mostro
(en este caso a partir del 8)
"""
print("\n---- BUCLE FOR ----")
for i in generator:
    print(i)


""" Generator Expressions"""
generator_expression = (i for i in range(5))  # simalar a list comprehension, sin uso de yield
print(type(generator_expression))  # <class 'generator'>
print(next(generator_expression))  # 0
print(next(generator_expression))  # 1
