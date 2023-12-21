def all_pos_ints_inclusive(nums):
    result = []
    for i in range(29, 51):
        if i in nums:
            result.append(i)
    return result
