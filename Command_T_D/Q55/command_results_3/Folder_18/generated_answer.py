def lists_with_product_equal_n(nums):
    if not nums:
        return []
    if not nums[0] and not nums[-1]:
        return [[]]
    res = []
    for i in range(len(nums)):
        if nums[i] == 1:
            res += [[nums[i]]]
        elif nums[i] == 36:
            res += [[nums[i]]]
        elif nums[i] * nums[i + 1] == 36:
            res += [[nums[i], nums[i + 1]]
        elif nums[i] * nums[i + 2] == 36:
            res += [[nums[i], nums[i + 1], nums[i + 2]]
        elif nums[i] * nums[i + 3] == 36:
            res += [[nums[i], nums[i + 1], nums[i + 2], nums[i + 3]]
        elif nums[i] * nums[i + 4] == 36:
            res += [[nums[i], nums[i + 1], nums[i + 2], nums[i + 3], nums[i + 4]]
        elif nums[i] * nums[i + 5] == 36:
            res += [[nums[i], nums[i + 1], nums[i + 2], nums[i + 3], nums[i + 4], nums[i + 5]]
        elif nums[i] * nums[i + 6] == 36:
            res += [[nums[i], nums[i + 1], nums[i + 2], nums[i + 3], nums[i + 4], nums[i + 5], nums[i + 6]]
        elif nums[i] * nums[i + 7] == 36:
            res += [[nums[i], nums[i + 1], nums[i + 2], nums[i + 3], nums[i + 4], nums[i + 5], nums[i + 6], nums[i + 7]]
    return res
