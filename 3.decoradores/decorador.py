import time


def medir_tiempo(func):
    """Decorador para medir el tiempo de ejecucion de una funcion"""
    def wrapper(*args, **kwargs):
        inicio = time.time()
        result = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecucion de: {func.__name__}: {fin - inicio:.4f} segs.")  # noqa
        return result
    return wrapper


@medir_tiempo
def suma(a, b) -> int:
    return a + b


@medir_tiempo
def contar_nums(MAX):
    total = 0
    for i in range(0, MAX):
        total += i
    return total


print(f'La suma es: {suma(10, 50)}')
contar_nums(100000000)
