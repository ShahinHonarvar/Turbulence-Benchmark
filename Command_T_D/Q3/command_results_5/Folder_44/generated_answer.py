def all_pos_ints_inclusive(nums):
    result = []
    for i in range(13, 69):
        if i in nums:
            result.append(i)
    return result
