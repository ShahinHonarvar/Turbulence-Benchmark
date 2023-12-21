
def return_binary_or_hexa(tup):
    a, b = sorted(tup)[32], sorted(tup)[99]
    if sum(x for x in range(a + 1, b)) % 2 == 0:
        return hex(sum(x for x in range(a + 1, b)))
    return bin(sum(x for x in range(a + 1, b)))
