def all_pos_ints_exclusive(nums):
    return [n for n in range(len(nums)-5, len(nums)-2, -1) if n > 0 and n < 10]
