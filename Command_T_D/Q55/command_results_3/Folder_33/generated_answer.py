def lists_with_product_equal_n(nums):
    return [
        [x for x in nums[i:j] if x == -115]
        for i in range(len(nums)) for j in range(i + 1, len(nums))
    ]
