from collections import deque


class Queue():
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        """Encolar un elemento al Queue"""
        self.items.append(item)

    def dequeue(self):
        """Elimina y retorna el primer elemento del frente del Queue"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()

    def peek(self):
        """Retorna el primer elemento del Queue"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def size(self):
        """Muestra el largo del Queue"""
        return len(self.items)


if __name__ == '__main__':
    queue = Queue()

    print(f"Personas en la cola: {queue.size()}")
    print('Llegan personas a la fila...')

    queue.enqueue('p1')
    queue.enqueue('p2')
    queue.enqueue('p3')

    print(f"Personas en la cola: {queue.size()}")           # 3

    print(f"\nAtentiendo a persona: {queue.dequeue()}")     # p1
    print(f"Personas en la cola: {queue.size()}")           # 2
    print(f"Siguiente persona: {queue.peek()}")             # p2

    print(f"\nAtentiendo a persona: {queue.dequeue()}")     # p2
    print(f"Personas en la cola: {queue.size()}")           # 1
    print(f"Siguiente persona: {queue.peek()}")             # p3

    print(f"\nAtentiendo a persona: {queue.dequeue()}")     # p3
    print(f"Personas en la cola: {queue.size()}")           # 0
    print(f"Siguiente persona: {queue.peek()}")             # IndexError: Queue is empty # noqa
