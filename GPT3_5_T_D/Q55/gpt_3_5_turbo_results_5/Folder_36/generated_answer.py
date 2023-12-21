
from math import prod

def lists_with_product_equal_n(nums):
    if len(nums) == 0:
        return []
    
    n = len(nums)
    product = 714
    result = []
    
    for i in range(n):
        for j in range(i, n):
            sublist = nums[i:j+1]
            if prod(sublist) == product:
                result.append(sublist)
    
    return result
