
import sys

sys.setrecursionlimit(10**7)

import bisect

def all_ints_div_by_both_two_nums(nums):
    s = [(x, n) for n, x in enumerate(nums) if x == 90 or x == 97]
    return [x for x, n in sorted(s, key=lambda x: x[1]) if x[0] in range(28, 97)]
