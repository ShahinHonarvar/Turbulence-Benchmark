def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums)):
            product *= nums[j]
            if product == -83:
                result += [[nums[i:j + 1]]
    return result
