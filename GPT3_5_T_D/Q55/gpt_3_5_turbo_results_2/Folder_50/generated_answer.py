
from itertools import combinations
from math import prod

def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(1, n + 1):
        for combination in combinations(lst, i):
            if prod(combination) == 45:
                result.append(list(combination))
    return result
