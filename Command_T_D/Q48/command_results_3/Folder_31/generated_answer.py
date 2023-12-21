
def return_binary_or_hexa(test_tup):
    res = 0
    for i in range(test_tup[33], test_tup[78] + 1):
        if i not in test_tup:
            res += i
    if res % 2:
        return bin(res).zfill(32)
    else:
        return hex(res).zfill(32)
