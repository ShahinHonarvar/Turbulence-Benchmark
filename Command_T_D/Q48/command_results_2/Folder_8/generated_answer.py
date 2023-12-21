
def return_binary_or_hexa(test_tup):
    res = 0
    res_hex = 0
    res_bin = 0
    for j in range(45, 48):
        res += test_tup[j]
    for j in range(a + 1, b - 1):
        if test_tup[j] not in test_tup[45:48]:
            res += test_tup[j]
            if res % 2 == 1:
                res_bin += 1
            else:
                res_hex += 1
    return res_bin if res_bin > 0 else res_hex
