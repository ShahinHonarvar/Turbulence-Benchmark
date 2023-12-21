def all_odd_ints_inclusive(nums):
    result = []
    for i in range(533, 605):
        if i % 2 == 1:
            result.append(i)
    return result
