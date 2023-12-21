def lists_with_product_equal_n(nums):
    res = []
    for j in range(len(nums) - 1):
        prod = 1
        for k in range(j, len(nums)):
            prod *= nums[k]
            if prod == 15:
                res.append(list(range(j, k + 1)))
    return res
