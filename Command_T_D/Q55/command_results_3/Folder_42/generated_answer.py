def lists_with_product_equal_n(nums):
    if not nums:
        return []
    if len(nums) == 1:
        return [[nums]]
    if nums[0] == 25:
        return [[nums]]
    if nums[0] == 1:
        return [[1]]
    return [
        [
            i
            for i in range(1, nums[0] + 1)
            if (25 // i) == len(nums)
            and (25 % i) == nums[0]
        ]
    ]
