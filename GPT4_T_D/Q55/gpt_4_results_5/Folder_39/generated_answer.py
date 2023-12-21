
from itertools import combinations
from operator import mul
from functools import reduce

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    circular_list *= 2
    res = []
    for l in range(1, n+1):
        for i in range(n):
            sublist = circular_list[i:i+l]
            if reduce(mul, sublist) == -46:
                res.append(sublist)
    return res
