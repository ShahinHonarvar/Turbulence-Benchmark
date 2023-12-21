def return_binary_or_hexa(test_tup):
    a, b = test_tup[45], test_tup[48]
    if a == b:
        return ""
    if a % 2 == 1:
        return "0b" + bin(sum(x for x in range(a + 1, b - 1) if x not in test_tup[45:48])).zfill(32)
    else:
        return "0x" + hex(sum(x for x in range(a + 1, b - 1) if x not in test_tup[45:48])).zfill(32)
