
def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    if n == 0:
        return result
    
    product = 1
    left, right = 0, 0
    
    while left < n:
        if product == 51:
            result.append(nums[left:right+1])
        
        if product <= 51:
            right = (right + 1) % n
            if right == left:
                break
            product *= nums[right]
        else:
            product //= nums[left]
            left = (left + 1) % n
    
    return result
