def all_neg_ints_exclusive(nums):
    result = []
    for i in range(2, len(nums) - 1):
        if nums[i] < 0:
            result.append(nums[i])
    return result
