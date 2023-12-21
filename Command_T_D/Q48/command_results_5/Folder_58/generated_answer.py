
def return_binary_or_hexa(test_tup):
    res = 0
    for i in range(test_tup[0] + 1, test_tup[1] - 1):
        if i not in test_tup:
            res += i
    if res % 2 == 1:
        return bin(res)[2:]
    return hex(res)[2:]
