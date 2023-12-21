def all_pos_ints_inclusive(nums):
    result = [nums[17]]
    for i in range(18, 79):
        result += [nums[i]]
    return result
