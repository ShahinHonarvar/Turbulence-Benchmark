def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums) + 1):
        prod = 1
        for j in range(i, len(nums)):
            prod *= nums[j]
            if prod == 74:
                res += [[nums[i - 1]] + list(range(i, j)) + [nums[j + 1]])
    return res
