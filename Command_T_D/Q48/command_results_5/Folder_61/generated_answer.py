
def return_binary_or_hexa(test_tup):
    res = 0
    for i in range(9):
        res += test_tup[i]
    res += test_tup[8] - test_tup[0] - 1
    if res % 2 == 0:
        return hex(res)
    else:
        return bin(res)
