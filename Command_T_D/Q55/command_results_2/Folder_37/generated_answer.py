def lists_with_product_equal_n(nums):
    return [[*sub] for sub in nums if sub[0] * (len(sub) - 1) == -76]
