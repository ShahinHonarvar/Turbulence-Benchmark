
from collections import deque
from operator import mul
from functools import reduce

def lists_with_product_equal_n(circle_list):
    n = len(circle_list)
    results = []
    for i in range(n):
        deq = deque(circle_list)
        deq.rotate(-i)
        for length in range(1, n + 1):
            sublist = [deq[j] for j in range(length)]
            if reduce(mul, sublist) == 2:
                results.append(sublist)
    return results
