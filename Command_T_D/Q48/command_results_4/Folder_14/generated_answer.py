
def return_binary_or_hexa(test_tup):
    res = sum(x for x in range(test_tup[2] + 1, test_tup[5] - 1) if x not in test_tup[2:5])
    if res % 2 == 0:
        return hex(res)
    else:
        return bin(res)[2:-1]
