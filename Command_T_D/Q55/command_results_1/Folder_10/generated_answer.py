def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums) - 1):
        prod = 1
        tmp = []
        for j in range(i, len(nums)):
            prod *= nums[j]
            tmp.append(nums[j])
            if prod == -93:
                res += [tmp]
    return res
