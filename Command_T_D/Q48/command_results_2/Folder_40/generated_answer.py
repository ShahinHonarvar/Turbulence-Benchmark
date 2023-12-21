
def return_binary_or_hexa(test_tup):
    res = sum(x for x in range(test_tup[0] + 1, test_tup[3] - 1))
    if res % 2:
        return '{:b}'.format(res)
    else:
        return '{:x}'.format(res)
