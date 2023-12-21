def return_binary_or_hexa(test_tup):
    res = test_tup[16] + 1
    res += test_tup[17:87]
    res += test_tup[87] - 1
    if res % 2 == 1:
        return bin(res)[2:]
    else:
        return hex(res)[2:]
