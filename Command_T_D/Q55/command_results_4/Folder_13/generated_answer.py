def lists_with_product_equal_n(nums):
    result = []
    for i in range(1, len(nums) + 1):
        if nums[i - 1] * i == 54:
            result.append(list(range(i, i + j + 1)))
    return result
