
def return_binary_or_hexa(test_tup):
    res = test_tup[20] + 1
    tmp = test_tup[93] - 1
    tmp = list(range(res, tmp, 2))
    if len(set(tmp)) != len(tmp):
        return '0b' + bin(sum(set(tmp)))[2:]
    else:
        return '0x' + hex(sum(tmp))[2:]
