
from collections import deque
from functools import reduce
import operator

def lists_with_product_equal_n(lst):
    if not lst:
        return []

    results = []
    q = deque(lst)
    for _ in range(len(lst)):
        sublist = []
        for i in range(len(lst)):
            sublist.append(q[i])
            if reduce(operator.mul, sublist, 1) == -15:
                results.append(sublist.copy())
        q.rotate(1)
    return results
