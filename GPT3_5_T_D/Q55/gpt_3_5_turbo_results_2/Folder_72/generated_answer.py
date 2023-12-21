
from itertools import cycle

def lists_with_product_equal_n(nums):
    if not nums:
        return []

    result = []
    product = 1
    start = 0

    for end in cycle(range(len(nums))):
        product *= nums[end]
        
        while product > 10:
            product //= nums[start]
            start = (start + 1) % len(nums)
            
        if product == 10:
            sublist = nums[start:end+1]
            result.append(sublist)

    return result
