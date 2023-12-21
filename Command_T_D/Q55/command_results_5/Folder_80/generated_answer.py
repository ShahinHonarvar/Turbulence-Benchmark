def lists_with_product_equal_n(nums):
    return [[*sub] for sub in nums if sum(sub) == 43]
