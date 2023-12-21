
def return_binary_or_hexa(test_tup):
    res = 0
    for i in range(test_tup[72] + 1, test_tup[93] - 1):
        if i not in test_tup:
            res += i
    if res % 2 == 0:
        return hex(res)
    else:
        return '0b' + bin(res)[2:]
