from collections import deque


class Stack():
    def __init__(self):
        self.items = deque()

    def __iter__(self):
        return reversed(self.items)

    def is_empty(self):
        """Valida si esta vacia el Stack"""
        return len(self.items) == 0

    def push(self, item):
        """Agrega el item al Stack"""
        self.items.append(item)

    def pop(self):
        """Elimina y retorna el ultimo Item del Stack"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Retorna el ultimo item del Stack"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        """Muestra el largo del Stack"""
        return len(self.items)

    def clear(self):
        """Elimina elementos del Stack"""
        self.items.clear()


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)

    print(stack.peek())  # 6

    print(stack.pop())  # 6
    print(stack.pop())  # 5
    print(stack.pop())  # 4

    print(stack.peek())  # 3

    stack.push(7)
    for i in stack:
        print(i)  # 7, 3, 2, 1
