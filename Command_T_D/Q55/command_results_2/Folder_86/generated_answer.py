import sys
from functools import reduce
from operator import mul
def lists_with_product_equal_n(nums):
    result = []
    for start in range(1, len(nums)):
        for stop in range(start, len(nums) + 1):
            for step in range(1, stop - start + 1):
                mult = reduce(mul, (nums[start:stop:step],))
                if mult == -779:
                    result += [[nums[start:stop:step]]
    return result
