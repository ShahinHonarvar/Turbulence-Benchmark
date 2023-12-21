
from collections import deque
from itertools import product

def lists_with_product_equal_n(lst):
    n = len(lst)
    sublists = []
    d = deque(lst)

    for _ in range(n):
        for i in range(1, n+1):
            sublist = list(d)[:i]
            if product(sublist) == -33:
                sublists.append(sublist)
        d.rotate(-1)

    return sublists
