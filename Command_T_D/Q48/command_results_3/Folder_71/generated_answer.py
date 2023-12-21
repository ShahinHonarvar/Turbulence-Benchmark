
def return_binary_or_hexa(test_tup):
    test_tup = sorted(test_tup)
    a = test_tup[20]
    b = test_tup[35]
    res = 0
    for i in range(a + 1, b - 1):
        if i not in test_tup:
            res += i
    if res % 2:
        return f"0b{res:b}"
    else:
        return f"0x{res:x}"
