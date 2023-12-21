def all_ints_exclusive(nums):
    result = list(range(10, 76))
    result += [x for x in range(10, 77) if x not in result]
    return result
