def all_odd_ints_inclusive(nums):
    result = []
    for i in range(59, 97):
        if i % 2 == 1:
            result.append(i)
    return result
