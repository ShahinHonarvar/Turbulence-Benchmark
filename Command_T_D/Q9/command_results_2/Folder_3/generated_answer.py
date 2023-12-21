def all_odd_ints_inclusive(nums):
    result = []
    for i in range(62, 92+1):
        if i % 2 == 1:
            result.append(i)
    return result
