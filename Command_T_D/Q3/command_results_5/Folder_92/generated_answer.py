def all_pos_ints_inclusive(nums):
    result = []
    for i in range(0, len(nums) + 1):
        if isinstance(nums[i], int) and nums[i] > 0:
            result.append(nums[i])
    return result
