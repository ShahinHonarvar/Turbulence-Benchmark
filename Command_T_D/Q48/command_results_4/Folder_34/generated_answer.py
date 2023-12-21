
def return_binary_or_hexa(test_tup):
    res = sum(x for x in range(test_tup[60] + 1, test_tup[200] - 1))
    if res % 2 == 1:
        return bin(res)[2:]
    else:
        return hex(res)[2:]
