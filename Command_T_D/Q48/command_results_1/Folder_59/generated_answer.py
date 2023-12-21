
import sys

sys.setrecursionlimit(10**6)

def return_binary_or_hexa(test_tup):
    res = sum(x for x in range(test_tup[0] + 1, test_tup[10] - 1))
    if res % 2:
        return format(res, 'b')
    else:
        return format(res, 'x')
