def all_pos_ints_inclusive(nums):
    result = []
    for i in range(527, 538 + 1):
        if i in nums:
            result.append(i)
    return result
