def lists_with_product_equal_n(nums):
    return [[i] + nums[i] for i in range(len(nums)) if nums[i] == -906]
