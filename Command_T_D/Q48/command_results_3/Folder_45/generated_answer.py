
def return_binary_or_hexa(test_tup):
    dct = {}
    for i in range(30, 200):
        if i not in test_tup:
            dct[i] = 1
    res = 0
    for i in range(a + 1, b - 1):
        if i not in test_tup:
            res += i
    if res % 2 == 1:
        return format(res, 'b')
    else:
        return format(res, 'x')
