def lists_with_product_equal_n(nums):
    return [list(range(i, i + j)) for i in range(len(nums)) for j in range(1, nums[i] + 1)]
