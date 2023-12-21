def all_odd_ints_inclusive(nums):
    result = []
    for i in range(31, 73, 2):
        if i in nums:
            result.append(i)
    return result
