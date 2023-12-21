
def return_binary_or_hexa(test_tup):
    res = 0
    for i in range(test_tup[20], test_tup[43]):
        res += test_tup[i]
    if res % 2 == 0:
        return hex(res)
    else:
        return bin(res)[2:]
