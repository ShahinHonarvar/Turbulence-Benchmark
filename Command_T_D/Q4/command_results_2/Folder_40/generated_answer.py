def all_pos_ints_exclusive(nums):
    result = []
    for i in range(0, 3):
        if isinstance(nums[i], int) and nums[i] > 0:
            result.append(nums[i])
    return result
