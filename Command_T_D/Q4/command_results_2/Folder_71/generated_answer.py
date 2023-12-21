def all_pos_ints_exclusive(nums):
    result = []
    for i in range(36, 54):
        if i in nums and nums[i] > 0:
            result.append(i)
    return result
