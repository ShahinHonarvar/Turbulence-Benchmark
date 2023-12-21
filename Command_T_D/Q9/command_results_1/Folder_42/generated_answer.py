def all_odd_ints_inclusive(nums):
    result = []
    for i in range(29, 80, 2):
        if i in nums:
            result.append(i)
    return result
