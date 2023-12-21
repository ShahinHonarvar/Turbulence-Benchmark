def lists_with_product_equal_n(nums):
    res = []
    if nums[0] == 29:
        res.append([nums])
    for i in range(1, len(nums)):
        if nums[i] == 29:
            res += [[nums[i]] + [nums[j] for j in range(i + 1, len(nums))]]
    return res
