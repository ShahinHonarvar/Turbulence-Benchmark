
def return_binary_or_hexa(tup):
    a, b = tup[35], tup[64]
    s = sum(n for n in range(a + 1, b - 1) if n not in tup[35:64])
    if s % 2:
        return format(s, 'b')
    else:
        return format(s, 'x')
