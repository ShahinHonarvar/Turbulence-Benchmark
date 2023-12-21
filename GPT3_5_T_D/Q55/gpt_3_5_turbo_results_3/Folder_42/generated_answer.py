
from itertools import cycle

def lists_with_product_equal_n(nums):
    size = len(nums)
    product = 1
    start = 0
    sublists = []
    
    for end in range(size + 1):
        while product > 25 and start < end:
            product //= nums[start]
            start += 1
        
        if product == 25:
            sublists.append(nums[start:end])
        
        if end < size:
            product *= nums[end]
    
    return sublists
