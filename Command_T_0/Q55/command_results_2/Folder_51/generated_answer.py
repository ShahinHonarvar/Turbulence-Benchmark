def lists_with_product_equal_n(nums):
    return [[nums[i:j] for i in range(len(nums)) if nums[i] * nums[i + 1] == -44] for j in range(i + 1, len(nums)) if nums[i] * nums[j] == -44]
