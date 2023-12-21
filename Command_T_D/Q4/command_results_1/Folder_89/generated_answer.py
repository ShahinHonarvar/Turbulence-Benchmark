def all_pos_ints_exclusive(nums):
    result = []
    for i in range(51, 77):
        if i in nums:
            result.append(i)
    return result
