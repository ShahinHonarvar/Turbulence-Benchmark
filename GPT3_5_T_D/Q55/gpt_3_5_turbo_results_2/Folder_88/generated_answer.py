
from itertools import combinations

def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for size in range(1, n+1):
        for start in range(n):
            sublist = lst[start:start+size]
            if len(sublist) < size:
                sublist += lst[:start+size-n]
            if reduce(lambda x, y: x*y, sublist) == -56:
                result.append(sublist)
                break
    return result
