def lists_with_product_equal_n(nums):
    if nums[0] == 0:
        return []
    if nums[0] == 1:
        return [[nums[0]]]
    sublists = []
    for i in range(1, len(nums)):
        if nums[i] == 0:
            break
        for j in range(i + 1, len(nums)):
            if nums[j] == 0:
                break
            if nums[i] * nums[j] == -906:
                sublists += [[nums[i], nums[j]]
    return sublists
