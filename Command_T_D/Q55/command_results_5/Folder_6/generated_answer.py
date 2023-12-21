def lists_with_product_equal_n(nums):
    return [[nums[i:j + 1] for i in range(len(nums) - 1) if nums[i:j + 1] == [42] * len(nums[i:j + 1])] for j in range(len(nums) - 1)]
