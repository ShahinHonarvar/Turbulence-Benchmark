def all_pos_ints_exclusive(nums):
    result = []
    for i in range(28, 49):
        if i in nums:
            result.append(i)
    return result
