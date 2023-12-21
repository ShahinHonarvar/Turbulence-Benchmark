def lists_with_product_equal_n(nums):
    result = []
    for i in range(1, len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] * nums[j] * nums[k] == 100:
                    result.append(list(range(i, k + 1)))
    return result
