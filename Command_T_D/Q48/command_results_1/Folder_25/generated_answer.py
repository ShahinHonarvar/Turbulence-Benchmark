
def return_binary_or_hexa(test_tup):
    res = sum(x for x in range(test_tup[37] + 1, test_tup[43] - 1) if x not in test_tup)
    if res % 2 == 1:
        return bin(res)[2:-1]
    else:
        return hex(res)[2:]
