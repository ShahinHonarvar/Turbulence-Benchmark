def all_pos_ints_inclusive(nums):
    result = []
    for i in range(len(nums) - 1):
        if nums[i] <= 62 and nums[i + 1] > 62:
            result.extend(list(range(nums[i] + 1, nums[i + 1] + 1)))
    return result
