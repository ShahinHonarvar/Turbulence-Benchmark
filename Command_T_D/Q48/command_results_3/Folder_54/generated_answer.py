
def return_binary_or_hexa(test_tup):
    a, b = 35, 64
    res = 0
    for i in range(a + 1, b - 1):
        if i not in test_tup:
            res += i
    if res % 2 == 1:
        return '0b' + bin(res).zfill(32)
    return '0x' + hex(res)[2:]
