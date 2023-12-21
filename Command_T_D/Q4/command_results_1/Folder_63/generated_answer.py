def all_pos_ints_exclusive(nums):
    result = []
    for i in range(38, 52):
        if i in nums and i > 0:
            result.append(i)
    return result
