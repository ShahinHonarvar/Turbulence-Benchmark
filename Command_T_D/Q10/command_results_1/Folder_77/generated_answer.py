def all_odd_ints_exclusive(nums):
    result = []
    for i in range(111, 473, 2):
        if i in nums:
            result.append(i)
    return result
