
def return_binary_or_hexa(test_tup):
    a, b = test_tup[90], test_tup[97]
    if a == b:
        return ""
    if a % 2 == 1:
        return "0b" + bin(sum(i for i in range(a + 1, b - 1)))[2:]
    return "0x" + hex(sum(i for i in range(a + 1, b - 1)))[2:]
