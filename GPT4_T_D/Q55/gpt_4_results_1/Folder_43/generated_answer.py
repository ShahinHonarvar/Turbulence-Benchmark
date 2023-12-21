
from copy import deepcopy
from functools import reduce
from operator import mul

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    if not n:
        return []
    sublists = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = circular_list[start: min(end, n)] + circular_list[:max(0, end - n)]
            if reduce(mul, sublist, 1) == -26:
                sublists.append(sublist)
    return sublists
