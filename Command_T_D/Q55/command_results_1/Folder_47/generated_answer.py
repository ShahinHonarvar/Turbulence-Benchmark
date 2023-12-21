def lists_with_product_equal_n(nums):
    res = []
    for a in range(1, len(nums)):
        b = nums[a]
        p = 1
        for c in range(a, b):
            p *= nums[c]
        if p == -94:
            res.append([nums[a], nums[b]])
    return res
