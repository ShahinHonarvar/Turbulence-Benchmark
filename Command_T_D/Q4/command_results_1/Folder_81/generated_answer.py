def all_pos_ints_exclusive(nums):
    result = []
    for i in range(10, 100):
        if i not in nums and i > 0:
            result.append(i)
    return result
