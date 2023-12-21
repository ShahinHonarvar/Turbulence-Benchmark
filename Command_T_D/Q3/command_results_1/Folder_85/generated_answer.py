def all_pos_ints_inclusive(nums):
    result = []
    for i in range(6, 8+1):
        if i in nums:
            result.append(i)
    return result
