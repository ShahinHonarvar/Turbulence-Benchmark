def all_pos_ints_inclusive(nums):
    return [x for x in range(0, min(nums)+1) if x in nums]
