
def return_binary_or_hexa(tup):
    a, b = tup[1], tup[8]
    s = sum(range(a + 1, b - 1))
    if s % 2 == 0:
        return hex(s)
    else:
        return bin(s)[2:]
