def lists_with_product_equal_n(nums):
    return [[nums[i:j + 1] for i in range(len(nums) - 1) if nums[i:j + 1].count(1) == 1] for j in range(1, len(nums))]
