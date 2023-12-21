def all_pos_ints_inclusive(nums):
    return [i for i in range(90, min(len(nums), 200), 1) if i in nums]
