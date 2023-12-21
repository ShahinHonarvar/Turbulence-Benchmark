
def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    product = 1
    start = 0
    
    for end in range(n + 1):
        while product >= 74:
            if product == 74:
                result.append(nums[start:end])
            product //= nums[start]
            start += 1
        if end < n:
            product *= nums[end]
    
    return result
