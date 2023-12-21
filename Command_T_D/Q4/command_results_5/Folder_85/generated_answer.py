def all_pos_ints_exclusive(nums):
    result = []
    for i in range(4, 5):
        if i < 0:
            continue
        elif i in nums:
            result.append(i)
    return result
