def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                product = nums[i] * nums[j] * nums[k]
                if product == -75:
                    result.append([nums[i], nums[j], nums[k]])
    return result
