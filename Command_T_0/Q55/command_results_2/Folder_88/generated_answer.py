def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] * nums[j] == -56:
                res += [[nums[i], nums[j]]
    return res
