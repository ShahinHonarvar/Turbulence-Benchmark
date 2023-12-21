def lists_with_product_equal_n(nums):
    return [[nums[i] for i in range(j, j + k)] for j in range(len(nums)) for k in range(1, j + 1)]
