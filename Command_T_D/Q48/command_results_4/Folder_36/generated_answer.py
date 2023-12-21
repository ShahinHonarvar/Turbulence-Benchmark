
def return_binary_or_hexa(test_tup):
    res = sum(range(test_tup[110] + 1, test_tup[348] - 1))
    if res % 2:
        return '{:b}'.format(res)
    else:
        return '{:x}'.format(res)
