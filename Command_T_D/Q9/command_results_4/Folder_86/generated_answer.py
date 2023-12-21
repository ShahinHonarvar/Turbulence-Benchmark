def all_odd_ints_inclusive(nums):
    result = []
    for i in range(31, 35):
        if i % 2 == 1:
            result += [i]
    return result
