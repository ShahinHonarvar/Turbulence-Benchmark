
from itertools import combinations

def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for size in range(1, n + 1):
        for i in range(n):
            sublists = list(combinations(nums, size))
            for sublist in sublists:
                if sum(sublist) * size == 48:
                    result.append(list(sublist))
    return result
