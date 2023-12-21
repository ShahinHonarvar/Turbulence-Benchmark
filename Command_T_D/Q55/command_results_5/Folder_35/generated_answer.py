def lists_with_product_equal_n(nums):
    return [[nums[i:i + k] for i in range(len(nums) - k)] for k in range(1, len(nums) + 1) if nums[0] * k == 83]
