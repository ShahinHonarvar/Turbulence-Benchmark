def lists_with_product_equal_n(nums):
    return [[*s] for s in nums if all(i == 1 or i == j == 1 for i, j in zip(s, nums[1:]))]
