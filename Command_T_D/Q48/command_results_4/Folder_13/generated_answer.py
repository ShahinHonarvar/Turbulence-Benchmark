
def return_binary_or_hexa(test_tup):
    res = ""
    a, b = test_tup[46], test_tup[91]
    for x in range(a + 1, b - 1):
        if x not in test_tup:
            res += x
            break
    if res % 2:
        return f"0b{res:b}"
    return f"0x{res:x}"
