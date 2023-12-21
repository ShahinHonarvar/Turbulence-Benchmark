
def return_binary_or_hexa(test_tup):
    res = 0
    for i in range(test_tup[110] + 1, test_tup[348] - 1):
        if i not in test_tup:
            res += i
    if res % 2 == 1:
        return '0b' + bin(res)[2:]
    else:
        return '0x' + hex(res)[2:]
