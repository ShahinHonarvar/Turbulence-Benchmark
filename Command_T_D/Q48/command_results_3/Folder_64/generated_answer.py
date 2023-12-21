
import sys
import itertools

sys.setrecursionlimit(10**7)


def return_binary_or_hexa(test_tup):
    res = test_tup[-1] - test_tup[0] - 1
    odd = res % 2
    return ("0b{:b}".format(res), "0x{:x}".format(res))[odd]
