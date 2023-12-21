import re
import sys
import itertools
def all_right_truncatable_prime(tup):
    res = []
    for i in range(1, tup[0]):
        if all(a % 10 == b for a, b in zip(str(i), range(1, 10))):
            res += [i]
    return res
