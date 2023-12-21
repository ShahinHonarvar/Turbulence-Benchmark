def all_neg_ints_exclusive(nums):
    result = []
    for i in range(0, len(nums) - 1):
        if nums[i] < 0:
            result.append(nums[i])
    for i in range(1, len(nums) - 1):
        if nums[i] < 0:
            result.append(nums[i])
    return result
