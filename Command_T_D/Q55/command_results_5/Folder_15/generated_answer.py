def lists_with_product_equal_n(nums):
    result = []
    current_product = 1
    for i in range(1, len(nums) + 1):
        current_product *= nums[i - 1]
        if current_product == -7:
            result += [[nums[i - 1]]
            current_product = 1
    return result
