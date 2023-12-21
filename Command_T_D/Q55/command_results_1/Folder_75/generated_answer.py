def lists_with_product_equal_n(nums):
    return [[nums[i:j] for i in range(len(nums)) if nums[i] * nums[j] == 13] for j in range(i, len(nums), 1) if nums[i] * nums[j] == 13]
