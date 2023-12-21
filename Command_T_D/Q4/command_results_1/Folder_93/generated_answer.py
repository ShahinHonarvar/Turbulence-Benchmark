def all_pos_ints_exclusive(nums):
    result = []
    for i in range(19, 95):
        if i in nums:
            result.append(i)
    return result
