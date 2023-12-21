
def return_binary_or_hexa(test_tup):
    a, b = test_tup[30], test_tup[200]
    res = sum(x for x in range(a + 1, b - 1) if x not in test_tup[30:200])
    if res % 2 == 0:
        return hex(res)
    else:
        return bin(res)
