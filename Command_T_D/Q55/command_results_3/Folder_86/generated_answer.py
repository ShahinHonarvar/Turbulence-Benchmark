def lists_with_product_equal_n(nums):
    if not nums:
        return []
    if len(nums) == 1:
        return [nums]
    if nums[0] == nums[-1] and nums[0] == -779:
        return [nums]
    for i in range(1, len(nums)):
        if nums[i] == nums[-1]:
            if nums[i] == -779:
                return [nums[:i], nums[i:]]
            if nums[0] == -779:
                return [nums[:i], nums[i+1:]]
            if nums[-1] == -779:
                return [nums[:i], nums[i+1:-1]]
    return []
