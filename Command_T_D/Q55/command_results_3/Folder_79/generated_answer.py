def lists_with_product_equal_n(nums):
    return [[x for x in nums[i:] if x == -83] for i in range(len(nums))]
