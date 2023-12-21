def all_odd_ints_inclusive(nums):
    result = []
    for i in range(40, 200, 2):
        if i in nums:
            result.append(i)
    return result
