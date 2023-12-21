
def return_binary_or_hexa(test_tup):
    a, b = test_tup[56], test_tup[88]
    res = sum(x for x in range(a + 1, b - 1) if x not in test_tup[56:88])
    if res % 2 == 0:
        return hex(res)
    else:
        return f'0b{res}'
