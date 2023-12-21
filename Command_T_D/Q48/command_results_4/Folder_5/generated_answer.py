
def return_binary_or_hexa(test_tup):
    res = ""
    test_tup = sorted(test_tup)
    a, b = test_tup[2], test_tup[8]
    if a == b:
        return ""
    elif (a + 1) % 2 == (b - 1) % 2:
        return "0b" + bin(a + 1 + (b - 1) // 2).zfill(16)
    else:
        return "0x" + hex(a + 1 + (b - 1) // 2)
