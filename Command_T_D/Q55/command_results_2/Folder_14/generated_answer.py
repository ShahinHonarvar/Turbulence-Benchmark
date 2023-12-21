def lists_with_product_equal_n(nums):
    return [list(range(start, end)) for start, end in zip(nums, nums[1:]) if (end - start) * (-72) == nums[0]]
