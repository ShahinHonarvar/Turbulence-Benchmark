
def return_binary_or_hexa(tup):
    a, b = tup[44], tup[91]
    s = sum(x for x in range(a + 1, b))
    if s % 2 == 0:
        return hex(s)
    else:
        return '{:b}'.format(s)
