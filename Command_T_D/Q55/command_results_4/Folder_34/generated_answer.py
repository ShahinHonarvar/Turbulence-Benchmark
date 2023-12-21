def lists_with_product_equal_n(nums):
    return [nums[i:j + 1] for i in range(len(nums)) for j in range(i, len(nums)) if nums[i] * nums[j] == -81]
