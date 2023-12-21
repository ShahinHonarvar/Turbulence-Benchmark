
def return_binary_or_hexa(test_tup):
    res = 0
    for x in range(test_tup[19] + 1, test_tup[32] - 1):
        if x not in test_tup[19:32]:
            res += x
    if res % 2:
        return bin(res).zfill(len(bin(res)) - 2)
    else:
        return hex(res)[2:]
