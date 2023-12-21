def all_pos_ints_exclusive(nums):
    result = [x for x in range(13, 77) if x in nums and x > 0]
    return result
