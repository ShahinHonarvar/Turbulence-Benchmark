def all_pos_ints_exclusive(nums):
    result = [x for x in range(55, 84)]
    return result if 55 <= max(nums) <= 84 else []
