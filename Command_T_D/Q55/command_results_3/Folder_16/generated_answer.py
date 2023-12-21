def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if nums[i] * nums[j] * nums[k] == -837:
                    result.append([nums[i], nums[j], nums[k]])
    return result
