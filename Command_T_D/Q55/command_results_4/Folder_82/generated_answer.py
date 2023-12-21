def lists_with_product_equal_n(nums):
    return [[i for i in nums[i:]] for i in range(len(nums)) if nums[i] * 7 == 8]
