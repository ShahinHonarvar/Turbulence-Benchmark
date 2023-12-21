def return_binary_or_hexa(test_tup):
    res = sum(range(test_tup[427] + 1, test_tup[669] - 1))
    if res % 2 == 0:
        return hex(res)
    else:
        return bin(res)
