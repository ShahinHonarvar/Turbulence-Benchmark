def return_binary_or_hexa(test_tup):
    a, b = test_tup[44], test_tup[91]
    if a == b:
        return ""
    if a % 2 == b % 2:
        return "0b" + bin(a + 1 + (b - a - 1) % 2).zfill(8)
    else:
        return "0x" + hex(a + 1 + (b - a - 1) % 2)
