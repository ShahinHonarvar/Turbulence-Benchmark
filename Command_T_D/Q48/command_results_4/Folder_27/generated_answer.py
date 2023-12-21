
def return_binary_or_hexa(test_tup):
    res = sum(x for x in range(test_tup[86] + 1, test_tup[89] - 1) if x not in test_tup)
    if res % 2:
        return format(res, 'b')
    else:
        return format(res, 'x')
