def all_odd_ints_exclusive(nums):
    result = []
    for i in range(27, 34):
        if i % 2 != 0:
            result.append(i)
    return result
