def lists_with_product_equal_n(nums):
    return [[nums[i:j] for i in range(len(nums) - 1) if (nums[i] * nums[i + 1] * nums[i + 2] * nums[i + 3] == -968)]]
