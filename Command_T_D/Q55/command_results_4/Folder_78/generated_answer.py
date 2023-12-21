def lists_with_product_equal_n(nums):
    return [[i] + [nums[i] for i in range(1, len(nums)) if nums[i] == nums[0]]
