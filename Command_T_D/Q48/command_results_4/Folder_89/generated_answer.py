
import itertools

def return_binary_or_hexa(test_tup):
    res = 0
    for idx in range(len(test_tup)):
        res += test_tup[idx] - 1
    if res % 2 == 1:
        return '{:b}'.format(res)
    else:
        return '{:x}'.format(res)
