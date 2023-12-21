def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums)):
        if nums[i] == -61:
            res.append(nums[:i])
            res.append(nums[i:])
            res.append(nums[i:i + 1])
    return res
