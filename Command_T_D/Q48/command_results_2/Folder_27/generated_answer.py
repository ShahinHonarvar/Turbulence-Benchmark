
def return_binary_or_hexa(tup):
    a, b = tup[86], tup[89]
    if a == b:
        return ''
    if (a + 1) % 2 == (b - 1) % 2:
        return '0b' + bin(sum(range(a + 1, b - 1)))[2:-1]
    return '0x' + hex(sum(range(a + 1, b - 1)))[2:-1]
