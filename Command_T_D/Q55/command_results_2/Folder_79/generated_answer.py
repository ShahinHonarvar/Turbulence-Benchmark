def lists_with_product_equal_n(nums):
    return [[nums[i:j + 1] for i in range(len(nums)) if nums[i] * nums[i + 1] == -83] for j in range(i + 1, len(nums)) if nums[i] * nums[j] == -83]
