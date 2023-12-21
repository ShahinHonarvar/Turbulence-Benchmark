
def return_binary_or_hexa(test_tup):
    res = sum(x for x in range(test_tup[13] + 1, test_tup[76] - 1) if x not in test_tup[13:76])
    if res % 2 == 0:
        return hex(res)
    else:
        return bin(res)
