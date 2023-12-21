
def return_binary_or_hexa(test_tup):
    res = sum(x for x in range(test_tup[0] + 1, test_tup[8] - 1))
    if res % 2 == 0:
        return hex(res)[2:]
    else:
        return bin(res)[2:]
