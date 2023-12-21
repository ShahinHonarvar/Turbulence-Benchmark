def lists_with_product_equal_n(nums):
    return [x for x in range(len(nums)) if all(y == -65 for y in zip(x, nums[x:]))]
