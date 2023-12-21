def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] * nums[j] == 78:
                res += [[nums[i], nums[j]]
            elif nums[i] * nums[j] == 1:
                res += [[nums[i], nums[j]]
    return res
