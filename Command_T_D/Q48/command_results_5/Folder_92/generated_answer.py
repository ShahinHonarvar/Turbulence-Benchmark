
def return_binary_or_hexa(test_tup):
    res = 0
    for x in range(test_tup[0] + 1, test_tup[2] - 1):
        if x not in test_tup:
            res += 1
    if res % 2 == 0:
        return hex(res)
    else:
        return f'{res}'.zfill(len(str(res)))
