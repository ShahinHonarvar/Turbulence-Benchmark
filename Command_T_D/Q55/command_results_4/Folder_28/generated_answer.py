def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums)):
        for j in range(i, len(nums)):
            prod = 1
            for k in range(i, j + 1):
                prod *= nums[k]
            if prod == 85:
                res.append(list(range(i, j + 1)))
    return res
