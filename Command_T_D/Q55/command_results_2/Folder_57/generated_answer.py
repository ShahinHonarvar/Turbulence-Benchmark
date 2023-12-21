def lists_with_product_equal_n(nums):
    return [[nums[i:j] for i in range(len(nums)) if prod(nums[i:j]) == -75] for j in range(i, len(nums) + 1)]
