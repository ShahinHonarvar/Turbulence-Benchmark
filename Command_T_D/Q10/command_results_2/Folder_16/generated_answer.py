def all_odd_ints_exclusive(nums):
    result = []
    for i in range(86, 90, 2):
        if i in nums:
            result.append(i)
    return result
