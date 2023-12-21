
def return_binary_or_hexa(tup):
    a, b = tup[86], tup[89]
    if (b - a - 1) % 2 == 1:
        return bin(a + 1 + (b - a - 1))
    else:
        return hex(a + 1 + (b - a - 1))
