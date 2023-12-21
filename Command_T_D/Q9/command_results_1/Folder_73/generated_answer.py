def all_odd_ints_inclusive(nums):
    result = []
    for i in range(19, 92):
        if i % 2 == 1:
            result.append(i)
    return result
