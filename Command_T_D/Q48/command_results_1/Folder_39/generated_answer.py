
def return_binary_or_hexa(test_tup):
    a, b = test_tup[44], test_tup[91]
    res = sum(range(a + 1, b - 1))
    return ("0b" + bin(res)[2:][-2::-2] if res % 2 else "0x" + hex(res)[2:][-4::-2])
