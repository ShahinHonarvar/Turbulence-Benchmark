
def return_binary_or_hexa(test_tup):
    res = 0
    for i in range(test_tup[6] + 1, test_tup[7] - 1):
        if i not in test_tup:
            res += i
    if res % 2 == 1:
        return bin(res).zfill(len(bin(res)))
    else:
        return hex(res).zfill(len(hex(res)))
