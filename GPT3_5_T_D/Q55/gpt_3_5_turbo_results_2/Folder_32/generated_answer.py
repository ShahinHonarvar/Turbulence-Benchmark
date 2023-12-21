
def lists_with_product_equal_n(nums):
    result = []
    nums_length = len(nums)
    
    for i in range(nums_length):
        product = 1
        for j in range(i, i + nums_length):
            product *= nums[j % nums_length]
            if product == 76:
                result.append(nums[i:((j+1) % nums_length)])
    
    return result
