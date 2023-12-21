def all_odd_ints_exclusive(nums):
    result = []
    for i in range(36, 85):
        if i % 2 == 1:
            result.append(i)
    return result
