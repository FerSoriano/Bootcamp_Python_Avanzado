
from stack import Stack


def verificar_simbolos(cadena: str) -> bool:
    stack = Stack()
    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for c in cadena:
        if c in '([{':
            stack.push(c)
        elif c in ')]}':
            if stack.is_empty() or stack.pop() != pares[c]:
                return False
    return True


print(verificar_simbolos("({[])})"))    # false
print(verificar_simbolos("({[]})"))     # true
print(verificar_simbolos("()"))         # true
print(verificar_simbolos("({([)})"))    # false
