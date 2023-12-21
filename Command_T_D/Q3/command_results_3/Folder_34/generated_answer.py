def all_pos_ints_inclusive(nums):
    result = [x for x in range(60, min(len(nums), 200) + 1)]
    return result if result else []
