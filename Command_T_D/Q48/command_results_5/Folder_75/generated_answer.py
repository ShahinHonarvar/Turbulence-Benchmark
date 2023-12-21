
def return_binary_or_hexa(test_tup):
    res = 0
    for i in range(20, 51):
        if test_tup[i] not in test_tup[20:51]:
            res += test_tup[i]
    if res % 2 == 0:
        return hex(res)
    else:
        return bin(res)[2:-1]
