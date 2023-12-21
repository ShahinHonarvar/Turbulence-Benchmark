def lists_with_product_equal_n(nums):
    if not nums:
        yield []
    for x in nums:
        for sublist in lists_with_product_equal_n(nums[1:]):
            if x * sublist[0] == 42:
                yield [x] + sublist
