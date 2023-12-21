
def lists_with_product_equal_n(nums):
    size = len(nums)
    result = []
    target = 85
    
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            product *= nums[end % size]
            
            if product == target:
                sublist = nums[start:end % size + 1]
                result.append(sublist)
    
    return result
