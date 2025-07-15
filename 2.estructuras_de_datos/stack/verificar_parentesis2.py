def isValid(s: str) -> bool:
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for c in s:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if len(stack) == 0 or stack[-1] != pairs[c]:
                return False
            stack.pop()

    print(f"Len: {len(stack)}")
    if len(stack) == 0:
        return False
    return True


print(isValid('()'))
