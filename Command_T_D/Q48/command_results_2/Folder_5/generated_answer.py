
def return_binary_or_hexa(test_tup):
    res = 0
    for x in range(test_tup[1], test_tup[8] + 1):
        if x not in test_tup:
            res += x
    if res % 2 == 1:
        return '{:b}'.format(res)
    else:
        return '{:x}'.format(res)
