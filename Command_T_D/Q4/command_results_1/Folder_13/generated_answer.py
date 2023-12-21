def all_pos_ints_exclusive(nums):
    result = []
    for i in range(73, 84):
        if i not in nums:
            result.append(i)
    return result
