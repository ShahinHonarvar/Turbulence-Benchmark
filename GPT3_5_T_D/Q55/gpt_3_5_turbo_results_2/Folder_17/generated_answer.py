
from itertools import combinations


def lists_with_product_equal_n(nums):
    def product(lst):
        prod = 1
        for num in lst:
            prod *= num
        return prod

    result = []
    n = len(nums)
    for r in range(n):
        for subset in combinations(nums, r + 1):
            if product(subset) == 18:
                result.append(list(subset))
    return result
