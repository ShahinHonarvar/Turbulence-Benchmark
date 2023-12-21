def lists_with_product_equal_n(nums):
    return [list(nums[i:i + j]) for i in range(len(nums)) for j in range(1, min(i + 1, len(nums) - i)) if len(list(nums[i:i + j])) == len(nums) and list(nums[i:i + j]) == sorted(list(nums[i:i + j]))]
