def all_pos_ints_exclusive(nums):
    result = [x for x in range(4, len(nums) - 1) if x > 0]
    return result
