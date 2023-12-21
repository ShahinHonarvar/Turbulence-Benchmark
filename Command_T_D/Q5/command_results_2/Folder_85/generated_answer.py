def all_neg_ints_inclusive(nums):
    result = []
    start, stop = 6, 8
    while start <= stop:
        if nums[start] < 0:
            result.append(nums[start])
        start += 1
    return result
