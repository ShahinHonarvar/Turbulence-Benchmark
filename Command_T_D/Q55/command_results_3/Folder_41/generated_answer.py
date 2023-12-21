def lists_with_product_equal_n(nums):
    return [[nums[i:j] for i in range(len(nums)) for j in range(i, len(nums)) if nums[i:j] * nums[j] == -20]]
