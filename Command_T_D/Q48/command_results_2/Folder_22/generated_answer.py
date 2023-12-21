
def return_binary_or_hexa(test_tup):
    a, b = test_tup[40], test_tup[200]
    res = 0
    for i in range(a + 1, b):
        if i not in test_tup:
            res += i
    if res % 2 == 1:
        return f"0b{res:b}"
    else:
        return f"0x{res:x}"
