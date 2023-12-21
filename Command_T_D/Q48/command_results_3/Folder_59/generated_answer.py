
def return_binary_or_hexa(test_tup):
    res = test_tup[10] - test_tup[0] - 1
    if res % 2 == 1:
        return format(res, 'b')
    else:
        return format(res, 'x')
