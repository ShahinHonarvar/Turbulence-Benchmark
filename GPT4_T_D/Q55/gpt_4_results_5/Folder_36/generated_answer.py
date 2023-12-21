
from collections import deque
from functools import reduce
from operator import mul
import itertools

def lists_with_product_equal_n(lst):
    n = len(lst)
    circular_list = deque(lst)
    result = []
    for i in range(n):
        for length in range(1, n+1):
            sublist = list(itertools.islice(circular_list, 0, length))
            if reduce(mul, sublist) == 714:
                result.append(sublist)
        circular_list.rotate(-1)
    return result
