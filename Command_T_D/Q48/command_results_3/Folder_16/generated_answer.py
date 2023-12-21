
def return_binary_or_hexa(test_tup):
    res = test_tup[90] + 1
    res += test_tup[92] - test_tup[91]
    res += test_tup[94] - test_tup[93]
    res += test_tup[96] - test_tup[95]
    if (res & 1) == 0:
        return hex(res)
    else:
        return bin(res)[2:-1]
