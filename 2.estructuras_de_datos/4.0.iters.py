import os

"""
Podemos crear objetos iteradores utilizando
el dunder method __iter__.
"""
class MyObject():  # noqa: E302 / evita el error del PEP
    def __init__(self):
        self.numeros = [1, 2, 3, 4, 5]

    def __iter__(self):  # se inicializa el iterador
        return iter(self.numeros)


# Iteramos el objeto sin llamar explicitamente a self.numeros
for num in MyObject():
    print(num)


"""
Ejemplo usando __iter__ en un Stack
"""
class Stack():  # noqa: E302
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        """Agregar un nuevo elemento"""
        self.items.append(item)

    def pop(self):
        """Eliminar y retornar el utlimo elemento."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Obtener el ultimo elemento"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        if self.is_empty():
            raise IndexError("clear form empty stack")
        self.items.clear()

    def __iter__(self):
        return reversed(self.items)


stack = Stack()
print("\tInicializando Stack...")
input()
while (True):
    print("\n1) Agregar")
    print("2) Eliminar")
    print("3) Ver ultimo Item")
    print("4) Ver largo del Stack")
    print("5) Mostrar Stack")
    print("6) Limpiar Stack")
    print("7) Salir\n")
    opcion = int(input("Opcion: "))

    match opcion:
        case 1:
            os.system("clear")
            item = input("\nItem: ")
            stack.push(item)
        case 2:
            os.system("clear")
            print(f"\nElemento eliminado: {stack.pop()}\n")
        case 3:
            os.system("clear")
            print(f"\nUltimo elemento: {stack.peek()}\n")
        case 4:
            os.system("clear")
            print(f"\nLargo: {stack.size()}\n")
        case 5:
            os.system("clear")
            if (stack.is_empty()):
                print("\nNo hay elementos en el Stack\n")
                continue
            for i in stack:
                print(i)
        case 6:
            os.system("clear")
            stack.clear()
            print("Stack eliminado")
        case 7:
            print("\n\tFin del programa")
            break
        case _:
            print("\nOpción no válida.")
