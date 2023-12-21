def all_pos_ints_inclusive(nums):
    result = []
    for i in range(21, 97):
        if i in nums:
            result.append(i)
    return result
