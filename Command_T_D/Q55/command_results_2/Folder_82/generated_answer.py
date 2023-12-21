def lists_with_product_equal_n(nums):
    return [list(sub) for i, sub in enumerate(zip(nums, nums[1:])) if all(x == 8 for x in zip(sub, range(1, len(sub) + 1)))]
