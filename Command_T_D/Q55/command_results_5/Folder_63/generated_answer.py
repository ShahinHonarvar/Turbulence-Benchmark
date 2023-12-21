def lists_with_product_equal_n(nums):
    return [[nums[0]] + [num for num in nums[1:]] + [nums[-1]]
