def all_pos_ints_inclusive(nums):
    result = []
    for i in range(62, 63 + 1):
        if i > 0 and i in nums:
            result.append(i)
    return result
