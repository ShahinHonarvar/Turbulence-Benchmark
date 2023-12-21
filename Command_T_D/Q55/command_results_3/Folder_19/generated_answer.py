def lists_with_product_equal_n(nums):
    res = []
    if not nums:
        res.append([])
        return res
    current_product = 1
    for i in range(len(nums)):
        current_product *= nums[i]
        if current_product == -54:
            res.append([nums[i], nums[i + 1 :]])
            current_product = 1
    return res
