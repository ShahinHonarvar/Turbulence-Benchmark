def all_pos_ints_inclusive(nums):
    result = []
    for i in range(0, 4):
        if i in nums and i > 0:
            result.append(i)
    return result
