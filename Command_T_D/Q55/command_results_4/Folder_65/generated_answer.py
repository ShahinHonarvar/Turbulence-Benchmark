def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        j = nums[i]
        while j != i:
            j = nums[j]
        res.append(nums[i:j])
    return res
