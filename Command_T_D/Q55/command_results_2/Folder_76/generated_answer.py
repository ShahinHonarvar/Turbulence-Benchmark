def lists_with_product_equal_n(nums):
    return [[x for x in nums[i:j]] for i in range(len(nums)) for j in range(i, len(nums)) if nums[i:j] * 247 == 247]
