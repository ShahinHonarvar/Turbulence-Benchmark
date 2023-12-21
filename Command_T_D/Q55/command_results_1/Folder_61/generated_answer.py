def lists_with_product_equal_n(nums):
    if not nums:
        return []
    if nums[0] * nums[-1] == -10:
        return [[nums]]
    return [[nums[i:j]] for i in range(len(nums)) for j in range(i + 1, len(nums) + 1)]
