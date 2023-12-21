def lists_with_product_equal_n(nums):
    return [nums[i:j + 1] for i in range(0, len(nums) - 1) for j in range(i + 1, len(nums)) if nums[i] * nums[j] == -690]
