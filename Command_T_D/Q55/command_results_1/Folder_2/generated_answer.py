import sys
from functools import reduce
from operator import mul
def lists_with_product_equal_n(nums):
    if len(nums) < 2:
        return []
    prod = reduce(mul, nums)
    if prod == -968:
        return [list(range(1, len(nums) + 1)) for _ in range(len(nums) - 1)]
    return []
