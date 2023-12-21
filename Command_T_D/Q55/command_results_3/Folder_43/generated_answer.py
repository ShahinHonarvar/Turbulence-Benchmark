def lists_with_product_equal_n(nums):
    result = []
    product = 1
    for i in range(len(nums)):
        product *= nums[i]
        if product == -26:
            result.append(list(range(i, len(nums))))
            product = 1
    return result
