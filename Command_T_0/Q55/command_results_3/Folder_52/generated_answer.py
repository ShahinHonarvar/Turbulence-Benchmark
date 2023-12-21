def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            prod = 1
            for k in range(i, j):
                prod *= nums[k]
            if prod == 37:
                res += [[nums[i], nums[j]]
    return res
