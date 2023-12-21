def all_pos_ints_exclusive(nums):
    result = []
    start, end = 56, 92
    for i in range(start, end):
        if i in nums and i > 0:
            result.append(i)
    return result
