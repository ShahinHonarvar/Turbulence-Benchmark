
from itertools import combinations

def lists_with_product_equal_n(nums):
    result = []
    length = len(nums)
    
    for i in range(1, length + 1):
        for j in range(length):
            sublist = nums[j:j+i]
            if sublist and reduce(lambda x, y: x * y, sublist) == -81:
                result.append(sublist)   
    
    return result
