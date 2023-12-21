
def return_binary_or_hexa(test_tup):
    res = 0
    for i in range(test_tup[44], test_tup[78] - 1):
        res += 1
        if res in test_tup:
            break
    if res in test_tup:
        return ''
    else:
        if res % 2:
            return bin(res).zfill(len(bin(res)))
        else:
            return hex(res).zfill(len(hex(res)))
