"""
Los Diccionarios en Python aceptan como clave solo valores de tipo INMUTABLE:
    - Strings
    - Entreros
    - Tuplas
No se aceptan tipos MUTABLES como listas.

Ejemplo Strings INMUTABLES
    nombre = "Fernando"
    nombre[0] = "A"
    print(nombre) # TypeError: 'str' object does not support item assignment
"""

my_dict = {
    "nombre": "Fernandno",
    (0, 1): "A"  # Se aceptan tuplas
}
print(my_dict)
