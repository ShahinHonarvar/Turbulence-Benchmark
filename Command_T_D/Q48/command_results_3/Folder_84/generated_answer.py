
import itertools

def return_binary_or_hexa(test_tup):
    res = 0
    for x in range(test_tup[32], test_tup[44] - 1):
        if x not in test_tup:
            res += x
    if res % 2:
        return '{:b}'.format(res)
    else:
        return '{:x}'.format(res)
