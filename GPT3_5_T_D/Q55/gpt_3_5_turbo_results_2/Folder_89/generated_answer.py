
def lists_with_product_equal_n(nums):
    size = len(nums)
    result = []
    
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            product *= nums[j % size]
            if product == 57:
                result.append(nums[i: j + 1])
    
    return result
