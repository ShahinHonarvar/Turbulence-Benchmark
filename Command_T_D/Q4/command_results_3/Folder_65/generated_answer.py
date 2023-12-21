def all_pos_ints_exclusive(nums):
    result = [nums[i] for i in range(len(nums)) if i != 42 and i != 87 and nums[i] > 0]
    return result
