def all_pos_ints_exclusive(nums):
    result = []
    for i in range(86, 90):
        if i not in nums:
            result.append(i)
    return result
