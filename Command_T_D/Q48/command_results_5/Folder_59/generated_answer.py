
def return_binary_or_hexa(test_tup):
    res = 0
    for i in range(11):
        res += test_tup[i]
    res += test_tup[0] + test_tup[10]
    if res % 2 == 1:
        return format(res, 'b')
    else:
        return format(res, 'x')
