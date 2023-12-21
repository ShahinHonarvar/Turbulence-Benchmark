def all_odd_ints_exclusive(nums):
    result = []
    for i in range(66, 90, 2):
        if i in nums:
            result.append(i)
    return result
