
def return_binary_or_hexa(test_tup):
    res = test_tup[10] + 1
    test_tup_str = str(test_tup)
    for x in range(11, 80):
        if str(test_tup[x]) not in test_tup_str:
            res += test_tup[x]
    if res % 2 == 0:
        return hex(res)
    return f'{res:b}'
