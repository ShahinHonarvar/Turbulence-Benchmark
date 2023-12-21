def all_pos_ints_inclusive(nums):
    result = []
    for i in range(30, 200):
        if i in nums:
            result.append(i)
    return result
