
def lists_with_product_equal_n(nums):
    result = []
    product = 1
    start = 0
    
    for end in range(len(nums) + 1):
        while product > 632 and start < end:
            product /= nums[start]
            start += 1
        
        if product == 632:
            result.append(nums[start:end])
        
        if end < len(nums):
            product *= nums[end]
    
    return result
