
from itertools import combinations

def lists_with_product_equal_n(nums):
    n = len(nums)
    sublists = []
    for size in range(1, n+1):
        for i in range(n):
            sublist = nums[i:i+size] + nums[:i+size-n]
            if prod(sublist) == -54:
                sublists.append(sublist)
    return sublists

def prod(lst):
    result = 1
    for num in lst:
        result *= num
    return result
