
from itertools import combinations

def lists_with_product_equal_n(nums):
    n = len(nums)
    sublists = []
    
    for size in range(1, n+1):
        for i in range(n):
            sublist = nums[i:i+size]
            if len(sublist) == size and product(sublist) == -16:
                sublists.append(sublist)
    
    return sublists

def product(nums):
    result = 1
    for num in nums:
        result *= num
    return result
