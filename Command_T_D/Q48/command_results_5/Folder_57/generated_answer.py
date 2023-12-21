
def return_binary_or_hexa(tup):
    a, b = tup[25], tup[80]
    if a == b:
        return ""
    res = sum(x for x in range(a + 1, b - 1))
    if res % 2 == 1:
        return format(res, 'b')
    return format(res, 'x')
