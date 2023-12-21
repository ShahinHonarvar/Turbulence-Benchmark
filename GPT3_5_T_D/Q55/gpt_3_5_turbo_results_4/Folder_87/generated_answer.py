
from itertools import cycle

def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    
    for i in range(n):
        temp_result = []
        product = 1
        for j in range(n):
            num = nums[(i+j) % n]
            product *= num
            temp_result.append(num)
            
            if product == 27:
                result.append(temp_result[:])
                
    return result
