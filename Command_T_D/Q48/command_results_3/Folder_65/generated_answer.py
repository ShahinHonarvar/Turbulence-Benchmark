
def return_binary_or_hexa(test_tup):
    res = 0
    for x in range(test_tup[51] + 1, test_tup[76] - 1):
        if x not in test_tup[51:76]:
            res += x
    if res % 2 == 1:
        return '{:b}'.format(res)
    else:
        return '{:x}'.format(res)
