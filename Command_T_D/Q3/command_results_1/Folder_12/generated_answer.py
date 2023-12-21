def all_pos_ints_inclusive(nums):
    return [i for i in range(max(nums), min(nums) - 1, -1) if i > 0]
