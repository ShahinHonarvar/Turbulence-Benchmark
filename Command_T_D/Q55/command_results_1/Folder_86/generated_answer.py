def lists_with_product_equal_n(nums):
    return [[nums[i] for i in range(j, j + k)] for j in range(len(nums) - 1) for k in range(1, min(len(nums) - j, 10) + 1)]
