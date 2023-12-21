
def return_binary_or_hexa(test_tup):
    res = 0
    for i in range(45, 48):
        res += test_tup[i]
    if res % 2:
        return format(res, 'b')
    else:
        return format(res, 'x')
