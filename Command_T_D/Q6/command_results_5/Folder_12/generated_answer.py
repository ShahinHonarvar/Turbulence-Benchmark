def all_neg_ints_exclusive(nums):
    result = []
    for i in range(len(nums) - 22):
        if nums[i] < 0:
            result.append(nums[i])
    for j in range(len(nums) - 24):
        if nums[j] < 0:
            result.append(nums[j])
    return result
