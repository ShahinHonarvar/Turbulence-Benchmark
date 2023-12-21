def all_pos_ints_exclusive(nums):
    result = []
    for i in range(44, 78):
        if i in nums and nums[i] > 0:
            result.append(i)
    return result
