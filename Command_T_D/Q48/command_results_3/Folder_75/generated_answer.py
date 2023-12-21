
def return_binary_or_hexa(tup):
    a, b = sorted(tup)[20], sorted(tup)[51]
    if a == b - 1:
        return ""
    res = sum(x for x in range(a + 1, b - 1) if x not in tup)
    if res % 2:
        return f'{res:b}'
    return f'{res:x}'
