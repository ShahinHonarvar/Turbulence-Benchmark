
def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    product = 1
    left = 0
    right = 0
    
    while left < n:
        while right < 2 * n and product * nums[right % n] <= 76:
            product *= nums[right % n]
            right += 1
            if product == 76:
                result.append(nums[left:right % n])
        product //= nums[left]
        left += 1
    
    return result
