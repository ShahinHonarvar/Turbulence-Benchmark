
def return_binary_or_hexa(test_tup):
    res = sum(x for x in range(test_tup[0] + 1, test_tup[4] - 1))
    if res % 2 == 0:
        return hex(res)
    else:
        return f'{res:b}'
