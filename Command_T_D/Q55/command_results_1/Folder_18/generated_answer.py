def lists_with_product_equal_n(nums):
    if not nums:
        return []
    return [nums[i:j] for i in range(len(nums)) for j in range(i, len(nums) + 1)]
