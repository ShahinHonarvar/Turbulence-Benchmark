def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums)):
        for j in range(i, len(nums)):
            prod = 1
            for k in range(i, j):
                prod *= nums[k]
            if prod == 4:
                res += [[nums[i:j+1]]
    return res
