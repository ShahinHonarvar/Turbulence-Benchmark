
def return_binary_or_hexa(test_tup):
    a, b = test_tup[10], test_tup[79]
    if a == b:
        return ""
    return ("0b" + bin(sum(x for x in range(a + 1, b - 1) if x not in test_tup))[2:]) if a & 1 else hex(sum(x for x in range(a + 1, b - 1) if x not in test_tup))
