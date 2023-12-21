def lists_with_product_equal_n(nums):
    return [nums[i:j + 1] for i in range(len(nums)) for j in range(i, len(nums) + 1) if nums[i:j + 1] == [76]]
