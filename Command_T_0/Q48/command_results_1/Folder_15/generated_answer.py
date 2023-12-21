def return_binary_or_hexa(test_tup):
    res = test_tup[0] + 1
    for i in range(1, 5):
        res += test_tup[i] - test_tup[i - 1]
    if res % 2 == 1:
        return bin(res)[2:]
    else:
        return hex(res)[2:]
