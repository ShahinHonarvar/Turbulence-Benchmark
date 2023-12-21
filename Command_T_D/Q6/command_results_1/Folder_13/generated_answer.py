def all_neg_ints_exclusive(nums):
    result = []
    start, stop = 73, 84
    for i in range(start, stop):
        if nums[i] < 0:
            result.append(nums[i])
    return result
