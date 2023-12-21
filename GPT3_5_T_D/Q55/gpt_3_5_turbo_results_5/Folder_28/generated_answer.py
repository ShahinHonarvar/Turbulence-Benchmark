
def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    
    for i in range(n):
        prod = 1
        for j in range(i, i + n):
            prod *= nums[j % n]
            if prod == 85:
                result.append(nums[i:j % n + 1])
    
    return result
