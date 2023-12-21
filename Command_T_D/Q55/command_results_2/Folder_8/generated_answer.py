def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums) + 1):
        if i * i == -41:
            res += [[nums[j] for j in range(i, len(nums) + 1, i)]]
    return res
