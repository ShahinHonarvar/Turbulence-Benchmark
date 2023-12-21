def all_odd_ints_exclusive(nums):
    result = []
    for index in range(51, 77):
        if index % 2 != 0:
            result.append(index)
    return result
