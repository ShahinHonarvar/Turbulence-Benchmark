def lists_with_product_equal_n(nums):
    if not nums:
        yield []
    else:
        yield [nums[0]] + [nums[1:]] + [nums[0:]]
