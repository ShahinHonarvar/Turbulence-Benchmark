
def return_binary_or_hexa(test_tup):
    res = test_tup[44] + 1
    res += test_tup[91] - test_tup[44] - 1
    if res % 2 == 1:
        return format(res, 'b')
    else:
        return format(res, 'x')
