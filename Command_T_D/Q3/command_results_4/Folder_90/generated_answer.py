def all_pos_ints_inclusive(nums):
    return [x for x in range(max(nums) + 1, 746, 1) if x > 0]
