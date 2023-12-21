def all_pos_ints_exclusive(nums):
    result = [n for n in range(40, 200) if n > 0 and n in nums]
    return result
