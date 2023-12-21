
def return_binary_or_hexa(test_tup):
    a, b = test_tup[450], test_tup[905]
    res = sum(x for x in range(a + 1, b))
    if res % 2 == 0:
        return hex(res)
    else:
        return bin(res)[2:]
