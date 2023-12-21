def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums)):
        for j in range(i, len(nums)):
            prod = 1
            cnt = 0
            for k in range(i, j):
                prod *= nums[k]
                cnt += 1
            if prod == -30:
                res += [[nums[i:j + 1]] * cnt]
    return res
