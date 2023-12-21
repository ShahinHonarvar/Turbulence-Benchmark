def lists_with_product_equal_n(nums):
    return [[nums[i:j + 1] for i in range(len(nums) - 1) if product(nums[i:j + 1]) == 76] for j in range(1, len(nums) - 1)]
