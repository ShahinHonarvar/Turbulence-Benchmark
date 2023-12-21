def return_binary_or_hexa(test_tup):
    res = test_tup[275] + 1
    res += test_tup[871] - test_tup[275] - 1
    if res % 2 == 1:
        return bin(res)[2:]
    else:
        return hex(res)[2:]
