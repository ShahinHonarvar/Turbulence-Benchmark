def lists_with_product_equal_n(nums):
    return [
        [nums[i] for i in range(j, j + i + 1)]
        for j in range(0, len(nums) - 1)
        if nums[j] == 47
    ]
