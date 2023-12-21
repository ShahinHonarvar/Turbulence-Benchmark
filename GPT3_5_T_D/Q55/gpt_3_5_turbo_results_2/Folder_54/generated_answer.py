
from itertools import accumulate, chain
from operator import mul

def lists_with_product_equal_n(nums):
    size = len(nums)
    nums.extend(nums)
    products = list(accumulate(nums, mul))
    sublists = []
    
    for i in range(size):
        for j in range(i+1, size+1):
            sublist_product = products[j]//products[i]
            if sublist_product == -17:
                sublists.append(nums[i:j])
            elif sublist_product == 1:
                break
    
    return sublists
