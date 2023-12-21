def all_pos_ints_exclusive(nums):
    result = []
    for i in range(0, 5):
        if i not in nums and nums[i] > 0:
            result.append(i)
    return result
