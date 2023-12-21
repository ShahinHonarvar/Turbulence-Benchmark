def all_pos_ints_exclusive(nums):
    result = []
    for i in range(0, 4):
        if i in nums and nums[i] > 0:
            result.append(nums[i])
    return result
