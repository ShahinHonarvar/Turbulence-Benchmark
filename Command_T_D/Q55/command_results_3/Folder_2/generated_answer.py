def lists_with_product_equal_n(nums):
    return [[*nums[i:]] for i in range(len(nums)) if nums[i] == -968]
