def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            prod = nums[i] * nums[j]
            if prod == -41:
                res.append(list(range(i, j + 1)))
    return res
