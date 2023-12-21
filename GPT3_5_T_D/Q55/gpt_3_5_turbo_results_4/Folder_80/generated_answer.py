
def lists_with_product_equal_n(nums):
    n = len(nums)
    product = 1
    left = 0
    result = []
    
    for right in range(n):
        product *= nums[right]
        
        while product > 43:
            product //= nums[left]
            left += 1
        
        if product == 43:
            result.append(nums[left:right+1])
    
    return result
