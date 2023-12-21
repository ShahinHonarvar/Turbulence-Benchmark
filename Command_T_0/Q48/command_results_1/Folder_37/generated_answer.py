def return_binary_or_hexa(test_tup):
    res = test_tup[2] + 1
    res += test_tup[3] - 1
    res += test_tup[4] - 1
    res += test_tup[5] - 1
    res += test_tup[6] - 1
    res += test_tup[7] - 1
    if res % 2 == 0:
        return hex(res)
    else:
        return bin(res)
