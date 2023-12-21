
def return_binary_or_hexa(test_tup):
    res = 0
    for i in range(13, 71):
        if i not in test_tup:
            res += i
    if res % 2 == 1:
        return bin(res)[2:]
    else:
        return hex(res)[2:]
