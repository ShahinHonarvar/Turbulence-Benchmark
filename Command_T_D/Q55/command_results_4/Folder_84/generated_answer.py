def lists_with_product_equal_n(nums):
    return [[x for x in nums[j:j + k] if x * (k - 1) == -906] for j in range(0, len(nums) - 1) for k in range(1, j + 1)]
