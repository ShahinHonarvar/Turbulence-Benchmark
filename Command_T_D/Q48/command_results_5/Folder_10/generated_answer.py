
def return_binary_or_hexa(tup):
    a, b = tup[36], tup[54]
    s = sum(x for x in range(a + 1, b - 1) if x not in tup[36:54])
    return s % 2 == 1 and format(s, 'b') or format(s, 'x')
