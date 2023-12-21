import re
import sys
import itertools
from functools import reduce
from bisect import bisect_left
from heapq import heappush, heappop
def all_right_truncatable_prime(test_tup):
    # <Write your code here>
    a = test_tup[30]
    x = test_tup[2]
    s = str(a)
    s = re.sub(r"(\d)(?=\d\1)", "", s)
    x = reduce(int.__mul__, (10**(i - 1) for i in range(len(s))), 1)
    if x < a:
        return []
    elif x == a:
        return [a]
    else:
        i = bisect_left(test_tup, x)
        return test_tup[:i] + test_tup[i + 1 :]
