def all_odd_ints_exclusive(nums):
    result = []
    for index in range(49, 75):
        if index % 2 == 1:
            result.append(index)
    return result
