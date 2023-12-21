def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        prod = 1
        for j in range(i, len(nums)):
            prod *= nums[j]
            if prod == 83:
                res.append(list(range(i, j + 1)))
    return res
