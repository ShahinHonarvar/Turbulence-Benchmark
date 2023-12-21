def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums)):
        s = nums[i]
        for j in range(i + 1, len(nums)):
            s *= nums[j]
            if s == 53:
                res.append(list(range(i, j + 1)))
    return res
