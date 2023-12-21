def lists_with_product_equal_n(nums):
    if nums[0] == 0:
        yield []
    for i in range(len(nums)):
        yield [nums[i]] + [nums[i + 1]]
