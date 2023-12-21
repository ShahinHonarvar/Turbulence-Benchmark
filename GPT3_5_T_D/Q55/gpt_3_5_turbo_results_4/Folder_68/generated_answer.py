
from itertools import cycle

def lists_with_product_equal_n(nums):
    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    
    sublists = []
    for i, num in enumerate(nums):
        curr_product = 1
        for j, next_num in enumerate(cycle(nums[i:])):
            curr_product *= next_num
            if curr_product == 6:
                sublists.append(nums[i:i+j+1])
            elif curr_product > 6:
                break
    
    return sublists
