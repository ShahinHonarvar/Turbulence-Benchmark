
def return_binary_or_hexa(test_tup):
    res = str(sum(x for x in range(test_tup[0] + 1, test_tup[1] - 1) if x not in test_tup))
    if res.isdigit():
        return hex(int(res))
    return f'{res}'
