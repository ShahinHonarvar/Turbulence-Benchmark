def all_pos_ints_exclusive(nums):
    result = []
    for i in range(18, 60):
        if i in nums and i > 0:
            result.append(i)
    return result
