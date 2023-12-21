def all_neg_ints_inclusive(nums):
    result = []
    start, stop = -60, -200
    while start <= stop:
        if start < len(nums) and nums[start] < 0:
            result.append(nums[start])
        start += 1
    return result
