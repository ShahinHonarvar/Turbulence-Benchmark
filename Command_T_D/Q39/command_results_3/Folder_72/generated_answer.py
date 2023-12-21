import sys
def return_n_greatest_chars(s):
    sys.setrecursionlimit(10**6)
    from bisect import bisect
    from heapq import heapify, heappop
    from itertools import accumulate
    import re
    return re.findall(r'[a-z]', s)[bisect(list(accumulate(list(re.findall(r'[a-z]', s))), 37):-1]
