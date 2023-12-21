
def return_binary_or_hexa(test_tup):
    res = sum(x for x in range(test_tup[29] + 1, test_tup[53] - 1))
    if res % 2 == 0:
        return hex(res)
    return bin(res)
