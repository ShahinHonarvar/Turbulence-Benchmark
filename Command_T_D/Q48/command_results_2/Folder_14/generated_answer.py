
def return_binary_or_hexa(test_tup):
    res = test_tup[2] + 1
    for i in range(test_tup[2] + 1, test_tup[5] - 1):
        if i not in test_tup:
            res += 1
    if res % 2 == 1:
        return bin(res).zfill(res.bit_length() + 1)
    return hex(res)[2:]
