def all_odd_ints_inclusive(nums):
    result = []
    for i in range(90, 201, 2):
        if i in nums:
            result.append(i)
    return result
