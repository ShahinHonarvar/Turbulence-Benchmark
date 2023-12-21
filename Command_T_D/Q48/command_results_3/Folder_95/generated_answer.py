
def return_binary_or_hexa(test_tup):
    a, b = test_tup[32], test_tup[99]
    test_tup = sorted(test_tup)
    test_tup = set(test_tup)
    if a + 1 <= b - 1 and (a + 1, b - 1) not in test_tup:
        if not (a + 1) & 1:
            return hex(a + 1)
        else:
            return hex(a + 1) + "b" + bin(b - 1 - a - 1)[2:]
    else:
        return ""
